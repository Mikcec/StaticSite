
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props  


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        # Add a leading space before the attributes string
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())


    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if not self.value:
            raise ValueError("invalid HTML: no value")
        
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    

    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: no tag")
        if not self.children:
            raise ValueError("invalid HTML: no children")
        
        children_html = ''.join(child.to_html() for child in self.children)

        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
