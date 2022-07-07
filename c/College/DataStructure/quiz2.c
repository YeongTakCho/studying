#include <stdio.h>
#include <stdlib.h>

char *s[15];
int cnt = 0;

struct node
{
    char *key;
    struct node *left, *right;
};

// Create a node
struct node *newNode(char *item)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}

// Inorder Traversal
void inorder(struct node *root)
{
    if (root != NULL)
    {
        // Traverse left
        inorder(root->left);

        // Traverse root
        printf("%s -> ", root->key);
        s[cnt] = root->key;
        cnt += 1;

        // Traverse right
        inorder(root->right);
    }
}

// Preorder traversal
void preorder(struct node *root)
{
    if (root == NULL)
        return;
    printf("%s ->", root->key);
    preorder(root->left);
    preorder(root->right);
}

// Postorder traversal
void postorder(struct node *root)
{
    if (root == NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%s ->", root->key);
}

// Insert a node
struct node *insert(struct node *node, char *key)
{
    // Return a new node if the tree is empty
    if (node == NULL)
        return newNode(key);

    // Traverse to the right place and insert the node
    if (key[0] < node->key[0])
        node->left = insert(node->left, key);
    else
        node->right = insert(node->right, key);

    return node;
}

// Insert on the left of the node
struct node *insertLeft(struct node *root, char *value)
{
    root->left = newNode(value);
    return root->left;
}

// Insert on the right of the node
struct node *insertRight(struct node *root, char *value)
{
    root->right = newNode(value);
    return root->right;
}

// Find the inorder successor
struct node *minValueNode(struct node *node)
{
    struct node *current = node;

    // Find the leftmost leaf
    while (current && current->left != NULL)
        current = current->left;

    return current;
}

// Deleting a node
struct node *deleteNode(struct node *root, char *key)
{
    // Return if the tree is empty
    if (root == NULL)
        return root;

    // Find the node to be deleted
    if (key[0] < root->key[0])
        root->left = deleteNode(root->left, key);
    else if (key[0] > root->key[0])
        root->right = deleteNode(root->right, key);

    else
    {
        // If the node is with only one child or no child
        if (root->left == NULL)
        {
            struct node *temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL)
        {
            struct node *temp = root->left;
            free(root);
            return temp;
        }

        // If the node has two children
        struct node *temp = minValueNode(root->right);

        // Place the inorder successor in position of the node to be deleted
        root->key = temp->key;

        // Delete the inorder successor
        root->right = deleteNode(root->right, temp->key);
    }
    return root;
}

// Driver code
int main()
{
    struct node *root1 = newNode("korea");

    insertLeft(root1, "data");
    insertRight(root1, "Ahn");
    insertLeft(root1->left, "quick");
    insertRight(root1->left, "sort");
    insertRight(root1->right, "university");
    insertLeft(root1->left->left, "bubble");
    insertLeft(root1->left->right, "algorithm");
    insertRight(root1->left->right, "computer");
    insertRight(root1->left->right->right, "recursive");
    insertLeft(root1->left->right->right->right, "tree");
    insertRight(root1->left->right->right->right, "hashO");
    insertLeft(root1->left->right->right->right->left, "chain");
    insertLeft(root1->left->right->right->right->left->left, "stack");
    insertRight(root1->left->right->right->right->left->left, "queue");
    // q1
    printf("\n=========================\n\nQuestion. 1\n");
    printf("\nInorder traversal: ");
    inorder(root1);
    printf("\nPreorder traversal: ");
    preorder(root1);
    printf("\nPostorder traversal: ");
    postorder(root1);

    struct node *root2 = NULL;

    for (int i = 0; i < (15); i++)
    {
        root2 = insert(root2, s[i]);
    }
    // q2
    printf("\n=========================\n\nQuestion. 2\n");
    printf("\nInorder traversal: ");
    inorder(root2);
    printf("\nPreorder traversal: ");
    preorder(root2);
    printf("\nPostorder traversal: ");
    postorder(root2);

    // q3
    printf("\n=========================\n\nQuestion. 3\n");
    printf("\nAfter deleting recursive\n");
    root2 = deleteNode(root2, "recursive");

    printf("\nInorder traversal: ");
    inorder(root2);
    printf("\nPreorder traversal: ");
    preorder(root2);
    printf("\nPostorder traversal: ");
    postorder(root2);
    printf("\n");
}