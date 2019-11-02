#include<stdio.h>
#define maxsize 10
typedef struct node{
char data;
struct node *lchild,*rchild;
} node;

typedef node *bitree;

typedef struct {
    bitree a[maxsize];
    int top;
}seqstack;

typedef struct{
    bitree a[maxsize];
    int ffront;
    int rear;
}seqqueue;

bitree buildtree()
{
    char c;
    node *p;
    c=getchar();
    if(c=='0')
    {
        p=NULL;
    }
    else
    {
           p=new(node);
           p->data=c;
           p->lchild=buildtree();
           p->rchild=buildtree();
    }
    return(p);
}

void preorder(bitree t)     //非递归前序
{
    seqstack s;
    s.top = -1; //置栈空
    while((t)||(s.top!=-1))
    {
        while(t)
        {
            printf("%c", t->data);
            s.top++;
            s.a[s.top] = t;
            t = t->lchild;
        }
        if (s.top>-1) {
            t = s.a[s.top];
            s.top--;
            t = t->rchild;
        }
    }
}

void DLR( node *root )      // 递归前序
{
    if (root!=NULL) //非空二叉树
    {   printf("%c",root->data); //访问D
            DLR(root->lchild); //递归遍历左子树
            DLR(root->rchild); //递归遍历右子树
    }
}

void midorder(bitree t)     // 非递归中序
{
    seqstack s;
    s.top = -1;//置栈空
    while((t)||(s.top!=-1))
    {
        while(t)
        {
            s.top++;
            s.a[s.top] = t;
            t = t->lchild;
        }
        t=s.a[s.top];
        printf("%c", t->data);
        s.top--;
        t=t->rchild;
    }
}

void LDR(node *root)        // 递归中序
{
    if(root !=NULL)
    {
            LDR(root->lchild);
            printf("%c",root->data);
            LDR(root->rchild);
    }
}

void postorder(bitree t)        // 非递归后序
{
    bitree lastvist;
    seqstack s;
    lastvist=0;
    s.top = -1;             //置栈空
    while(t||s.top != -1)
    {
        while(t)
        {
            s.top++;
            s.a[s.top]=t;
            t=t->lchild;
        }
        t=s.a[s.top];
        if(t->rchild==lastvist||t->rchild==NULL)
        {
            printf("%c", t->data);
            s.top--;
            lastvist=t;
            t=0;
        }
        else t=t->rchild;
    }
}

void LRD (node *root)       // 递归后序
{
    if(root !=NULL)
    {
        LRD(root->lchild);
        LRD(root->rchild);
        printf("%c",root->data);
    }
}

void LevelOrder(node *root)
{
    if(root==NULL)  return;             // 树空终止
    seqqueue q;
    node *r;
    q.ffront=0;                         // 初始化队列为空
    q.rear=0;
    q.a[q.rear++]=root;                 //¸根节点入队
    while(q.ffront!=q.rear)             // 队不空
    {
        if(q.rear+1==maxsize)   q.rear=0;
        r=q.a[q.ffront];
        q.ffront=(q.ffront+1)%maxsize;  // 队首出队并访问
        printf("%c",r->data);
        if(r->lchild)                   // 队首的左右孩子依次入队
        {
            q.a[q.rear]=r->lchild;
            q.rear=(q.rear+1)%maxsize;
        }
        if(r->rchild)
        {
            q.a[q.rear]=r->rchild;
            q.rear=(q.rear+1)%maxsize;
        }
    }
}

int main()
{
    bitree t;
    t=buildtree();   //测试 abc00d00e0fg000
    //printf("\n非递归前序遍历\n");
    //preorder(t);
    //printf("\n递归前序遍历\n");
    //DLR(t);
    //printf("\n非递归中序遍历\n");
    //midorder(t);
    //printf("\n递归中序遍历\n");
    //LDR(t);
    printf("\n非递归后序遍历\n");
    postorder(t);
    //printf("\n递归后序遍历\n");
    //LRD(t);
    //printf("\n层次遍历\n");
    //LevelOrder(t);
    printf("\n");
    return 0;
}
