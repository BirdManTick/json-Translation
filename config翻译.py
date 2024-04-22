from transformers import MarianMTModel, MarianTokenizer
i=0
# 加载预训练的 MarianMT 模型和 tokenizer


def translate_comment(comment):
    input_ids = tokenizer.encode(comment, return_tensors="pt")
    translated_ids = model.generate(input_ids)
    translation = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    return translation

def process_yaml_file(input_yaml_path, output_yaml_path):
    global i
    with open(input_yaml_path, 'r', encoding='utf-8') as input_file:
        with open(output_yaml_path, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                if '#' in line:  # 检查当前行是否有注释
                    # 分离内容和注释，并翻译注释
                    content, comment = line.split('#', 1)
                    translated_comment = translate_comment(comment.strip())
                    # 将内容、翻译后的注释写入新文件
                    output_file.write(f"{content.rstrip()}  # {translated_comment} \n")
                else:
                    # 如果没有注释，直接写入内容
                    output_file.write(line)
                i = i + 1
                print(i)
# 请将以下路径替换为你实际的YAML文件路径
input_yaml_path = input('config name:')
output_yaml_path = input_yaml_path[:-4]+'[new].yml'
# 调用函数处理YAML文件

model_name = './opus-mt-en-zh'
tokenizer = MarianTokenizer.from_pretrained(model_name, local_files_only=True)
model = MarianMTModel.from_pretrained(model_name, local_files_only=True)
process_yaml_file(input_yaml_path, output_yaml_path)
