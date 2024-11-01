import type Result from "@/typeutils/Result";
import type {Ref} from "vue";
import type ChatModel from "@/typeutils/ChatModel";
function arrayToMarkdownTable(data) {
    if (!Array.isArray(data) || data.length === 0) {
        return ''; // 如果输入不是数组或数组为空，返回空字符串
    }

    // 获取表头
    const headers = Object.keys(data[0]);
    const headerRow = `| ${headers.join(' | ')} |`;
    const separatorRow = `| ${headers.map(() => '---').join(' | ')} |`;

    // 获取数据行
    const rows = data.map(item => {
        return `| ${headers.map(header => item[header]).join(' | ')} |`;
    });

    // 组合所有行
    return [headerRow, separatorRow, ...rows].join('\n');
}
const steps = ['转化问题','自然语言转化','解析到SQL语句','SQL查询结果','最终回答','开始生成最终回答'] as const
export function SQLworkflow(data:Result<typeof steps[number]>,messages:Ref<Array<ChatModel>>){
//     第一步 转化问题
    if(data.message=='转化问题'){
        messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content + "## 转化问题\n"
        for (value in data.payload){
            messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content + `- ${value}\n`
        }

    }
    else if (data.message=='自然语言转化'){
         messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content+`\n ## 对子问题${data.payload}的SQL处理 \n`
    }
    else if (data.message == '解析到SQL语句'){
         messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content+`${data.payload}`
    }
    else if (data.message == 'SQL查询结果'){
        messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content+'\n ## SQL查询结果 \n'
        messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content+ arrayToMarkdownTable(data.payload)
    }
    else if (data.message=='开始生成最终回答'){
         messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content+'\n # 最终答案 \n'
    }
    else if (data.message=='最终回答'){
           messages.value[messages.value.length-1].content = messages.value[messages.value.length-1].content+ data.payload
    }

}