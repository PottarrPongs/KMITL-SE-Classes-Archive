trait Renderable {
    fn render(&self) -> String;
}

struct Button {
    label: String,
}

struct Label {
    text: String,
}

struct Container {
    name: String,
    children: Vec<Box<dyn Renderable>>,
}

// Helper: indent every line in `s` by one tab
fn indent_one_tab(s: &str) -> String {
    s.lines().map(|l| format!("\t{l}")).collect::<Vec<_>>().join("\n")
}

impl Renderable for Button {
    fn render(&self) -> String {
        format!("Button: [{}]", self.label)
    }
}

impl Renderable for Label {
    fn render(&self) -> String {
        format!("Label: '{}'", self.text)
    }
}

impl Renderable for Container {
    fn render(&self) -> String {
        // Render children first, then indent their lines
        let rendered_children = self
            .children
            .iter()
            .map(|c| c.render())
            .collect::<Vec<_>>()
            .join("\n");
        let indented = if rendered_children.is_empty() {
            String::new()
        } else {
            indent_one_tab(&rendered_children) + "\n"
        };

        format!("Container ('{}') {{\n{}}}", self.name, indented)
    }
}

fn main() {
    // Build inner container
    let mut inner_container = Container {
        name: "Login Form".to_string(),
        children: Vec::new(),
    };
    inner_container
        .children
        .push(Box::new(Label { text: "Username".to_string() }));
    inner_container
        .children
        .push(Box::new(Button { label: "Submit".to_string() }));

    // Heterogeneous list
    let mut screen: Vec<Box<dyn Renderable>> = Vec::new();
    screen.push(Box::new(Label { text: "Welcome to my App!".to_string() }));
    screen.push(Box::new(inner_container));
    screen.push(Box::new(Button { label: "Sign Out".to_string() }));

    println!("--- Rendering Screen ---");
    for component in screen {
        println!("{}", component.render());
    }
}
