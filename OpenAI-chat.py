from openai2 import Chat

api_key = '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'  # 更换成自己的api_key

talk_1 = Chat(api_key=api_key, model="gpt-3.5-turbo")
talk_2 = Chat(api_key=api_key, model="gpt-3.5-turbo")

talk_1.request('数字1的后面是几?')
# >>> 2

talk_2.request('数字101的后面是几?')
# >>> 102

talk_1.request('再往后是几?')
# >>> 3

talk_2.request('再往后是几?')
# >>> 103


talk_1.dump('./talk_record.json')




new_talk = Chat(api_key=api_key, model="gpt-3.5-turbo")
new_talk.load('./talk_record.json')
new_talk.request('再往后呢?')
# >>> 4




talk_4 = Chat(api_key=api_key, model="gpt-3.5-turbo")

talk_4.request('数字1的后面是几?')
# >>> 2

talk_4.request('再往后是几?')
# >>> 3

talk_4.request('再往后呢?')
# >>> 4

# 回滚
talk_4.rollback()
# >>> [user]: 再往后是几?
# >>> [assistant]: 3

# 再回滚
talk_4.rollback()
# >>> [user]: 数字1的后面是几?
# >>> [assistant]: 2

talk_4.request('再往后是几?')
# >>> 3