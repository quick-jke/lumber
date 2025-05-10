import re

def parse_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    pattern = re.compile(
        r'DATA\s+class\s+(\w+)\s*\{([^}]*)\}',
        re.DOTALL
    )

    matches = pattern.findall(content)
    classes = []

    for class_name, body in matches:
        fields = []
        lines = body.split(";")
        for line in lines:
            line = line.strip()
            if not line or line.startswith("//") or line.startswith("public:") or line.startswith("private:") or line.startswith("protected:"):
                continue

            parts = line.split()
            if len(parts) >= 2:
                field_type = " ".join(parts[:-1])
                field_name = parts[-1]
                fields.append((field_name, field_type))

        classes.append({
            "name": class_name,
            "annotations": ["DATA"],
            "fields": fields
        })

    return classes