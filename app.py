
def main():
    replace_words = {
        'reg_val_32_inst;':'reg_ptr;',
        'reg_val_32=0;': 'exp_reg_data;',
        'uvm_pkg::uvm_reg_data_t_read_field_vals[$];':'uvm_pkg::uvm_reg_data_t read_reg_data[$]'

                    }

    with open("code.txt",'r') as rf:
        with open("code_updated.txt",'w',encoding='utf-8') as wf:
            line = rf.read()
            for word in line.split():
                print(word)
                try:
                    line = line.replace(word, replace_words[word])
                except:
                    pass
            wf.write(line)



if __name__ == "__main__":
    main()