def get_graph(input_file,output_file):

    f = open(input_file, 'r')
    w = open(output_file, 'w')
    lines = f.readlines()
    # 競プロみたいな感じに点、辺の個数を表示
    n = 0
    m = 0
    for line in lines:
        if ":" in line:
            n += 1
        if "->" in line:
            m += 1
    w.write("{} {}\n".format(n,m))

    # CFH CPHが出力されないことがあることを考慮しています
    # TODO: なぜか片方しかハッシュがとれていないときにも対応する
    mode=""
    for line in lines:
        if ":" in line:
            parsed = line.split("[")
            vertex = parsed[0]
            class_method = parsed[1].split("\"")[1][0:-1]
            mode = "vertex"
        if mode == "vertex":

            if "CFH" in line:
                cfh = line.split("=")[1][0:-1]
            elif "CPH" in line:
                cph = line.split("=")[1][0:-4]
                mode=""
            elif "FH" in line:
                fh = line.split("=")[1][0:-1]
            elif "PH"in line:
                ph = line.split("=")[1][0:-1]
            if "]" in line and "CPH" in line:
                w.write("{} {} {} {} {} {}\n".format(class_method,vertex,fh,ph,cfh,cph))
                mode = ""
                cfh=""
                cph=""
            # なぜかハッシュが出力されていないときハッシュを-1に設定
            if "[" in line and "]" and ";" in line:
                class_method = parsed[1].split("\"")[1]
                print("{} {} {} {}".format(class_method,vertex,-1,-1))
        if "->" in line:
            mode = "edge"
            parsed_line = line.split("->")
            start_vertex = parsed_line[0]
            end_vertex = parsed_line[1].split(" ")[0]
            w.write("{} {}\n".format(start_vertex,end_vertex))
    f.close()
    w.close()

# get_graph(input_file = "twodot/2_flow_m_c_o_target.dot",output_file="./2fo2.txt")
get_graph(input_file = "twodot/2_flow_m_c_n_target.dot",output_file="./2fn2.txt")