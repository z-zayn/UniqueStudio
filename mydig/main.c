#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<netinet/in.h>
#include<unistd.h>

char dns_servers[1][16];    // 存放DNS服务器的IP
int dns_server_count = 0;


/*
**DNS报文中查询区域的查询类型
*/

#define A 1         // 查询类型
#define NS 2
#define CNAME 5
#define SOA 6

void ngethostbyname(unsigned char*, int);
void changetoDnsNameFormat(unsigned char*, unsigned char*);


/*
**DNS报文首部
**这里使用了位域
*/

struct DNS_HEADER {
    unsigned short id;      // 会话标识
    unsigned char rd :1;    // 表示期望递归
    unsigned char tc :1;    // 表示可截断的
    unsigned char aa :1;    // 表示授权回答
    unsigned char opcode :4;
    unsigned char qr :1;    // 查询/响应标志，0为查询，1为响应
    unsigned char rcode :4; // 应答码
    unsigned char z :1;     // 保留值
    unsigned char ra :1;    // 表示可用递归
    unsigned short q_count; // 表示查询问题区域节的数量
    unsigned short ans_count; // 表示回答区域的数量
    unsigned short auth_count; // 表示授权区域的数量
    unsigned short add_count; // 表示附加区域的数量
};


/*
**DNS报文中查询问题区域
*/

struct QUESTION {
    unsigned short qtype;//查询类型
    unsigned short qclass;//查询类
};

typedef struct {
    unsigned char *name;
    struct QUESTION *ques;
} QUERY;


#pragma pack(push, 1)   // 预编译命令设置1字节对齐
/*
**DNS报文中回答区域的常量字段
*/
struct R_DATA {
    unsigned short type;        // 表示资源记录的类型
    unsigned short _class;      // 类
    unsigned int ttl;           // 表示资源记录可以缓存的时间
    unsigned short data_len;    // 数据长度
};

#pragma pack(pop)
/*
**DNS报文中回答区域的资源数据字段
*/

struct RES_RECORD {
    unsigned char *name;    // 资源记录包含的域名
    struct R_DATA *resource;       //  资源数据
    unsigned char *rdata;
};


int main(int argc, char *argv[])
{
    unsigned char hostname[100];
    unsigned char dns_servername[100];
    // 默认dns服务器和请求类型
    strcpy(dns_servername, "202.114.0.131");
    int query_type = A;

    if (argc == 2)  // 只有一个参数必然是主机域名
        strcpy(hostname, argv[1]);
    else if (argc == 3)  // 两个参数分情况 域名加方式 指定DNS服务器加域名
    {
        if (strchr(argv[1], '@') == NULL)
        {
            strcpy(hostname, argv[1]);
            if (strchr(argv[2], 'a') || strchr(argv[2], 'A'))
                query_type = A;
            else if (strstr(argv[2], "ns") || strstr(argv[2], "NS"))
                query_type = NS;
        }
        else
        {
            strcpy(dns_servername, argv[1]+1);
            strcpy(hostname, argv[2]);
        }
    }
    else    // 三个参数
    {
        strcpy(dns_servername, argv[1]+1);
        strcpy(hostname, argv[2]);
        if (strchr(argv[3], 'a') || strchr(argv[3], 'A'))
            query_type = A;
        else if (strstr(argv[3], "ns") || strstr(argv[3], "NS"))
            query_type = NS;
    }
    strcpy(dns_servers[0], dns_servername);
//    printf("请输入要查询IP的主机名：");
//    scanf("%s", hostname);
//    strcpy(hostname, argv[1]);
    ngethostbyname(hostname, query_type);

    return 0;
}

/*
**实现DNS查询功能
*/

void ngethostbyname(unsigned char *host, int query_type) {

    unsigned char buffer[65536], *qname, *reader;
    int i, j, s;

    struct sockaddr_in a;       // 地址
    struct RES_RECORD answers[20], auth[20], addit[20];// 回答区域、授权区域、附加区域中的资源数据字段
    struct sockaddr_in dest;    // 地址

    struct DNS_HEADER *dns = NULL;
    struct QUESTION *qinfo = NULL;

    printf("\n所需解析域名：%s\n", host);

    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP); // 建立UDP套接字

    dest.sin_family = AF_INET;  // IPv4
    dest.sin_port = htons(53);  // 53号端口
    dest.sin_addr.s_addr = inet_addr(dns_servers[0]);   //DNS服务器IP
    // inet_addr 将一个ip字符串转化为一个网络字节序的整数值，用于sockaddr_in.sin_addr.s_addr
    dns = (struct DNS_HEADER *) &buffer;

    // 设置DNS报文首部
    dns->id = (unsigned short) htons(getpid()); // id设为进程标识符
    dns->qr = 0;        // 查询
    dns->opcode = 0;    // 标准查询
    dns->aa = 0;        // 不授权回答
    dns->tc = 0;        // 不可截断
    dns->rd = 1;        // 期望递归
    dns->ra = 0;        // 不可用递归
    dns->z = 0;         // 必须为0
    dns->rcode = 0;     // 没有差错
    dns->q_count = htons(1); // 1个问题
    dns->ans_count = 0;
    dns->auth_count = 0;
    dns->add_count = 0;

    // qname指向查询问题区域的查询名字段
    qname = (unsigned char *) &buffer[sizeof(struct DNS_HEADER)];

    changetoDnsNameFormat(qname, host); // 修改域名格式

    // qinfo指向问题查询区域的查询类型字段
    qinfo = (struct QUESTION *) &buffer[sizeof(struct DNS_HEADER) + (strlen((const char *) qname) + 1)];

    qinfo->qtype = htons(query_type); // 查询类型为A
    qinfo->qclass = htons(1); // 查询类一般设为1

    // 向DNS服务器发送DNS请求报文
    if (sendto(s, (char *) buffer,
               sizeof(struct DNS_HEADER) + (strlen((const char *) qname) + 1) + sizeof(struct QUESTION), 0,
               (struct sockaddr *) &dest, sizeof(dest)) < 0) {
        perror("发送报文失败！");
    }

    // 从DNS服务器接受DNS响应报文
    i = sizeof dest;
    if (recvfrom(s, (char *) buffer, 65536, 0, (struct sockaddr *) &dest, (socklen_t *) &i) < 0) {
        perror("接收报文失败！");
    }

    dns = (struct DNS_HEADER *) buffer;

    // 将reader指向接收报文的answer区域
    reader = &buffer[sizeof(struct DNS_HEADER) + (strlen((const char *) qname) + 1) + sizeof(struct QUESTION)];

    printf("\n响应报文包含: ");
    printf("\n QUERY:%d", ntohs(dns->q_count));
    printf("\n ANSWER:%d", ntohs(dns->ans_count));
    printf("\n AUTHORITY:%d", ntohs(dns->auth_count));
    printf("\n ADDITIONAL:%d\n\n", ntohs(dns->add_count));

    /*
    **解析接收报文
    */
    int ans_cont = ntohs(dns->ans_count);   // 解析所有的answer
    for (int i = 0; i < ans_cont; i++)
    {
        reader = reader + sizeof(int16_t);    // reader指向answer的查询类型字段
        answers[i].resource = (struct R_DATA *) reader;
        reader = reader + sizeof(struct R_DATA);    // 指向answer区域的资源数据字段
        printf("资源类型为 %d\n", ntohs(answers[i].resource->type));
        if (ntohs(answers[i].resource->type) == A || ntohs(answers[i].resource->type) == NS || ntohs(answers[i].resource->type) == CNAME)  // 判断资源类型
        {
            answers[i].rdata = (unsigned char *) malloc(ntohs(answers[i].resource->data_len));   // 资源数据
            for (j = 0; j < ntohs(answers[i].resource->data_len); j++) {
                answers[i].rdata[j] = reader[j];
            }
            answers[i].rdata[ntohs(answers[i].resource->data_len)] = '\0';
            reader = reader + ntohs(answers[i].resource->data_len);     // 如果answer不止一条reader指向下一条answer的开头
        }
        // 显示查询结果
        if (ntohs(answers[i].resource->type) == A) // 判断查询类型是否为A
        {
            long *p;
            p = (long *) answers[i].rdata;
            a.sin_addr.s_addr = *p;
            printf("IPv4地址:%s\n", inet_ntoa(a.sin_addr));
        }
        if (ntohs(answers[i].resource->type) == NS) // 判断查询类型是否为NS
        {
            long *p;
            p = (long *) answers[i].rdata;
            a.sin_addr.s_addr = *p;
            printf("NS记录:%s\n", inet_ntoa(a.sin_addr));
        }
        if (ntohs(answers[i].resource->type) == CNAME) // 判断查询类型是否为CNAME
        {
            long *p;
            p = (long *) answers[i].rdata;
            a.sin_addr.s_addr = *p;
            printf("CNAME记录:%s\n", inet_ntoa(a.sin_addr));
        }
    }

    int auth_cont = ntohs(dns->auth_count);
    for (int i=0; i<auth_cont; i++)
    {
        reader = reader + sizeof(int16_t);    // 这时reader指向auth区域的查询类型字段
        auth[i].resource = (struct R_DATA *) reader;
        reader = reader + sizeof(struct R_DATA);    // 指向auth区域的资源数据字段
        printf("资源类型为 %d\n", ntohs(auth[i].resource->type));
        if (ntohs(auth[i].resource->type) == A || ntohs(auth[i].resource->type) == NS || ntohs(auth[i].resource->type) == CNAME || ntohs(auth[i].resource->type) == SOA)  // 判断资源类型
        {
            auth[i].rdata = (unsigned char *) malloc(ntohs(auth[i].resource->data_len));   // 资源数据
            for (j = 0; j < ntohs(auth[i].resource->data_len); j++) {
                auth[i].rdata[j] = reader[j];
            }
            auth[i].rdata[ntohs(auth[i].resource->data_len)] = '\0';
            reader = reader + ntohs(auth[i].resource->data_len);     // 如果auth不止一条reader指向下一条auth的开头
        }
        // 显示查询结果
        if (ntohs(auth[i].resource->type) == A) // 判断查询类型是否为A
        {
            long *p;
            p = (long *) auth[i].rdata;
            a.sin_addr.s_addr = *p;
            printf("IPv4地址:%s\n", inet_ntoa(a.sin_addr));
        }
        if (ntohs(auth[i].resource->type) == NS) // 判断查询类型是否为NS
        {
            long *p;
            p = (long *) auth[i].rdata;
            a.sin_addr.s_addr = *p;
            printf("NS记录:%s\n", inet_ntoa(a.sin_addr));
        }
        if (ntohs(auth[i].resource->type) == CNAME) // 判断查询类型是否为CNAME
        {
            long *p;
            p = (long *) auth[i].rdata;
            a.sin_addr.s_addr = *p;
            printf("CNAME记录:%s\n", inet_ntoa(a.sin_addr));
        }
        if (ntohs(auth[i].resource->type) == SOA) // 判断查询类型是否为SOA
        {
            long *p;
            p = (long *) auth[i].rdata;
            a.sin_addr.s_addr = *p;
            printf("SOA记录:%s\n", inet_ntoa(a.sin_addr));
        }
    }
    printf("\nSERVER:\n%s#53(%s)\n", dns_servers[0], dns_servers[0]);
    printf("WHEN:\n");
    system("date");
    return;
}

/*
**改变域名格式 比如 从www.baidu.com转换到3www5baidu3com
*/

void changetoDnsNameFormat(unsigned char *qname, unsigned char *host)
{
    int flag = 0;
    strcat(host, ".");
    for (int i = 0; i < strlen(host); i++)
    {
        if (host[i] == '.')
        {
            *(qname++) = i - flag;

            for (; flag < i; flag++)
            {
                *(qname++) = host[flag];
            }
            flag++;
        }
    }
    *(qname++) = '\0';
}
