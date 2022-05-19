// 이진 검색 트리 삽입과 삭제 (child가 0인 경우, 1인 경우, 2인 경우)
// (3삭제, 30 삭제, 15삭제)
// 각각을 삭제한 후 In- order 출력
#include <stdio.h>
#include <stdlib.h>

struct nodeTree
{
    int key;
    struct nodeTree *left;
    struct nodeTree *right;
};

struct nodeTree *getNode(int v)
{
    struct nodeTree *newNode = malloc(sizeof(struct nodeTree));
    newNode->key = v;
    newNode->left = NULL;
    newNode->right = NULL;

    return newNode;
}

struct nodeTree *treeInsert(struct nodeTree *root, int val)
{

    if (root == NULL) // case1
        return getNode(val);

    if (root->key > val) // case 2
        root->left = treeInsert(root->left, val);

    else if (root->key < val) // case3
        root->right = treeInsert(root->right, val);

    return root;
}

void printInorder(struct nodeTree *root)
{
    if (root == NULL)
        return;
    printInorder(root->left);
    printf("%d ", root->key);
    printInorder(root->right);
}
int getMin(struct nodeTree *root) // 노드 삭제를 위한 보조 함수
{
    struct nodeTree *temp = root;

    while (temp->left != NULL)
    {
        temp = temp->left;
    }

    return temp->key;
}
struct nodeTree *removeNode(struct nodeTree *root, int val) //노드 삭제를 위한 함수
{
    if (root == NULL)
        return NULL;

    if (root->key < val)
        root->right = removeNode(root->right, val);

    else if (root->key > val)
        root->left = removeNode(root->left, val);

    else
    {
        if (root->left == NULL && root->right == NULL)
        {
            free(root);
            return NULL;
        }
        else if (root->left == NULL)
        {
            struct nodeTree *temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL)
        {
            struct nodeTree *temp = root->left;
            free(root);
            return temp;
        }
        else
        {
            int rightMin = getMin(root->right);
            root->key = rightMin;
            root->right = removeNode(root->right, rightMin);
        }
    }
    return root;
}

int main()
{
    struct nodeTree *root = NULL;
    root = treeInsert(root, 55);
    root = treeInsert(root, 15);
    root = treeInsert(root, 60);
    root = treeInsert(root, 8);
    root = treeInsert(root, 28);
    root = treeInsert(root, 90);
    root = treeInsert(root, 3);
    root = treeInsert(root, 30);
    root = treeInsert(root, 48);
    root = treeInsert(root, 38);
    root = treeInsert(root, 50);
    root = treeInsert(root, 33);
    root = treeInsert(root, 32);
    root = treeInsert(root, 36);

    removeNode(root, 3);
    printInorder(root);
    printf("\n");

    removeNode(root, 30);
    printInorder(root);
    printf("\n");

    removeNode(root, 15);
    printInorder(root);
    printf("\n");

    return 0;
}