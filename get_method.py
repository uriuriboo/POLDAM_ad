def get_method(file,method_name):
    f = open(file, 'r')
    lines = f.readlines()
    mode = ""
    code = ""
    brackets = 0

    for line in lines:
        # 空白を含んでも大丈夫なように
        trim_line = line.replace(" ","")
        if mode == "in_method":
            brackets += line.count('{')
            brackets -= line.count('}')
            code += line

            if brackets == 0:
                mode = "end_method"
                break

        elif method_name+"(" in trim_line  and ("public" in line or "private" in line or "protected" in line):
            method_name+"(" in trim_line  and ("public" in line or "private" in line or "protected" in line)
            mode = "in_method"

            brackets += line.count('{')
            brackets -= line.count('}')
            code += line

            if brackets == 0:
                mode = "end_method"
                break

        
    print(code)

method_name = "replaceTop"
file = "./JsonWriter.kt"

get_method(file,method_name)