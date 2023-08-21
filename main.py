#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Phương thức KnowledgeBase.declare xử lý các câu từ tệp đầu vào và điền vào cơ sở tri thức các sự kiện và quy tắc.
# Đối với mỗi query trong tệp truy vấn, hàm main truy xuất đối tượng Fact tương ứng đại diện cho truy vấn. 
# Hàm forward_chaining được gọi với truy vấn làm đầu vào và nó trả về một tập hợp các dữ kiện (sự thay thế) đáp ứng truy vấn. 
# Những kết quả này sau đó được định dạng và ghi vào output.

from KnowledgeBase import KnowledgeBase
from fact import Fact

def read_input_file():
    input_file = "BritishRoyalFamily.pl"
    with open(input_file, 'r') as f_input:
        sentences = f_input.readlines()
    return sentences

def read_query_file():
    query_file = "queries.txt"
    with open(query_file, 'r') as f_query:
        queries = f_query.readlines()
    return queries

def main():
    kb = KnowledgeBase()
    sentences = read_input_file()
    KnowledgeBase.populate(kb, sentences)

    queries = read_query_file()
    output_file = "answers.txt"
    with open(output_file, 'w') as f_output:
        for query_str in queries:
            alpha = Fact.parse_fact(query_str)
            alpha_str = str(alpha)
            substitutions = set(kb.query(alpha))
            print(alpha_str)
            subst_str = ' ;\n'.join([str(subst) for subst in substitutions]) + '.\n'
            f_output.write(alpha_str + '\n')
            f_output.write(subst_str + '\n')

if __name__ == "__main__":
    main()


# In[ ]:




