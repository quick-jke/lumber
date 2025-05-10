import os
import sys
from parser import parse_file
from generator import generate_code

def scan_directory(path):
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    else:
        output_dir = os.path.join("build", "generated")

    os.makedirs(output_dir, exist_ok=True)

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".hpp"):
                full_path = os.path.join(root, file)
                print(f"🔍 Scanning {full_path}")
                classes = parse_file(full_path)

                for cls in classes:
                    generated_code = generate_code(cls)

                    header_file = os.path.join(output_dir, f"{cls['name']}.hpp")
                    source_file = os.path.join(output_dir, f"{cls['name']}_generated.cpp")

                    with open(header_file, "w") as hfile:
                        guard = f"_{cls['name'].upper()}_HPP"
                        hfile.write(f"#ifndef {guard}\n")
                        hfile.write(f"#define {guard}\n\n")
                        hfile.write("#include <string>\n\n")
                        hfile.write("namespace quick {\n\n")
                        hfile.write("class ")
                        hfile.write(f"{cls['name']} {{\n")
                        hfile.write("public:\n")
                        
                        hfile.write("    // Constructors\n")
                        hfile.write(f"    {cls['name']}();\n")
                        args = ', '.join([f'{field_type} {field_name}' for field_name, field_type in cls['fields']])
                        hfile.write(f"    {cls['name']}({args});\n\n")
                        
                        for field_name, field_type in cls['fields']:
                            cap_name = field_name.capitalize()
                            hfile.write(f"    {field_type} get{cap_name}() const;\n")
                            hfile.write(f"    void set{cap_name}({field_type} value);\n")
                        hfile.write("\nprivate:\n")
                        for field_name, field_type in cls['fields']:
                            hfile.write(f"    {field_type} {field_name};\n")
                        hfile.write("};\n\n")
                        hfile.write("} // namespace quick\n\n")
                        hfile.write(f"#endif // {guard}\n")

                    with open(source_file, "w") as cppfile:
                        cppfile.write("// Auto-generated code — DO NOT EDIT\n")
                        cppfile.write(f"#include \"{cls['name']}.hpp\"\n\n")
                        cppfile.write("namespace quick {\n\n")
                        cppfile.write(generate_code(cls))
                        cppfile.write("\n} // namespace quick\n")

                    print(f"✅ Generated class '{cls['name']}' → {header_file} and {source_file}")

if __name__ == "__main__":
    scan_directory("examples")