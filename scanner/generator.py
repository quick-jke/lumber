def generate_code(cls):
    class_name = cls["name"]
    fields = cls["fields"]

    code = ""



    code += f"{class_name}::{class_name}() = default;\n\n"

    args = ", ".join([f"{t} {n}" for n, t in fields])
    init_list = ", ".join([f"{n}({n})" for n, t in fields])
    code += f"{class_name}::{class_name}({args}) : {init_list} {{}}\n\n"

    for field_name, field_type in fields:
        cap_name = field_name.capitalize()
        code += f"{field_type} {class_name}::get{cap_name}() const {{ return {field_name}; }}\n"
        code += f"void {class_name}::set{cap_name}({field_type} value) {{ {field_name} = value; }}\n\n"



    return code