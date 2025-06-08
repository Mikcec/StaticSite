from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodedelimiter import split_nodes_delimiter

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

main()