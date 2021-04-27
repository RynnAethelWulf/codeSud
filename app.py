
def main():
    # These are the word for replace in dictionary format
    replace_words = {
        'reg_val_32_inst;':'reg_ptr;',
        'reg_val_32=0;': 'exp_reg_data;',
        'uvm_pkg::uvm_reg_data_t_read_field_vals[$];':'uvm_pkg::uvm_reg_data_t read_reg_data[$]'

                    }
#  wOpen to read file code.text
    with open("code.txt",'r') as rf:
        # Open to write file to code_updated.txt
        with open("code_updated.txt",'w',encoding='utf-8') as wf:
            # read each line
            line = rf.read()
            for word in line.split():
                print(word)
                try:
                    # replacing word with correct words
                    line = line.replace(word, replace_words[word])
                except:
                    pass
                # At last writng to thge file
            wf.write(line)



if __name__ == "__main__":
    main()