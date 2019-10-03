# 功能

## 基础修改功能
增加单词和翻译
修改单词和翻译

## 背诵功能
随机给出单词/翻译（乱序背诵）
按字典序给出单词/翻译（顺序背诵）
    （记录上次背到的地方，可选择从头开始还是继续）

## 导入导出功能
导入单词和翻译
导出单词和翻译

## 统计功能
统计单词背过的次数
统计每天背过的单词数目
统计单词数量

## 查询功能
根据单词查翻译
输出所有单词和翻译


# 数据结构设计

## 单词表
```json
words_table {
    words(sds): {           // 单词，作为键
        translation(sds),   // 翻译
        show_counts(int),   // 背诵/展示次数
        search_counts(int), // 查询次数，包含通过单词/翻译进行查询
    }
    // other words
}
```

## 统计表
```json
date_info {
    someday(sds): {         // 日期，作为键
        recite_counts(int),   // 背诵单词数目
        add_counts(int),    // 增加单词数目
        del_counts(int),    // 删除单词数目
        mod_counts(int),    // 修改单词数目
    }
} 
base_info {
    last_time_mode,     // 上次背诵时的模式（顺序，乱序）
    last_time_pos,      // 上次顺序背诵时的最后一个单词位置
    last_time,          // 上次背单词的时间
}

```


# bug
1. Windows 下导入非 export 创建的 words.txt