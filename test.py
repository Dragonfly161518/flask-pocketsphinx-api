# -*- coding: utf-8 -*-

from pythainlp.summarize import summarize_text
# from pythainlp.spell.pn import correct as pn_tnc_correct
# from pythainlp.spell.pn import spell as pn_tnc_spell

# spell checker from pythainlp.spell module (generic)
text = 'เมื่อเวลา 00.30 น. วันที่ 8 ม.ค. 62 นายนรรัตน์ สกุลปทุมทอง อายุ 45 ปี วินจักรยานยนต์รับจ้างพื้นที่เมืองพัทยา ได้เดินทางเข้าแจ้งความร้องทุกข์ กับ ร.ต.อ.วีระยุทธ กางกาละ รอง สว.สอบสวน สภ.เมืองพัทยา ว่าสามารถเก็บกระเป๋าเงินได้ ซึ่งภายในมีเอกสารสำคัญและทรัพย์สินจำนวนมาก ได้ที่บริเวณริมถนน ปากซอย 6 หน้าธนาคารกรุงเทพ พัทยาสายสอง ต.หนองปรือ อ.บางละมุง จ.ชลบุรี ประสงค์ให้นำส่งคืนเจ้าของเมื่อตรวจสอบภายในกระเป๋าพบว่ามีเงินสกุลต่างประเทศจำนวนหลายวอน คิดเป็นเงินไทยประมาณ 40,000 บาท มีเอกสารสำคัญหลายรายการ และนามบัตรระบุเบอร์ติดต่อชัดเจน จึงได้โทรติดต่อให้มารับคืนที่สถานีตำรวจภูธรเมืองพัทยา ทราบชื่อผู้ที่เป็นเจ้าของคือ น.ส.พลับพรึง ทองคำ อายุ 41 ปี ได้ตรวจสอบทรัพย์สินพบว่าครบทุกบาท ไม่มีสูญหายแต่อย่างใดภายหลังจากที่ น.ส.พลับพรึง ทองคำ อายุ 41 ปี เจ้าของทรัพย์สินเดินทางมาถึงโรงพัก ถึงกับแสดงอาการดีใจเป็นอย่างมาก โดยกล่าวว่าไม่คิดว่าประเทศไทยจะมีคนดีแบบนี้ ตอนแรกคิดว่าจะแจ้งความเอกสารหายเท่านั้น แต่ปรากฏว่าได้ทรัพย์สินคืนทั้งหมดก็รู้สึกดีใจมาก ก่อนจะมอบสินน้ำใจให้กับนายนรรัตน์ สกุลปทุมทอง วินจักรยานยนต์รับจ้างน้ำใจงาม เป็นสินน้ำใจแทนคำขอบคุณด้วย'
print (summarize_text(text, 1, engine='frequency', tokenizer='newmm'))

# spell checker from pythainlp.spell.pn module (specified algorithm - Peter Norvig's)
# print(pn_tnc_spell("เหลืยม"))
# print(pn_tnc_correct("เหลืยม"))


# # spell checker from pythainlp.spell.pn module (specified algorithm, custom dictionary)
# ttc_word_freqs = ttc.word_freqs()
# pn_ttc_checker = NorvigSpellChecker(custom_dict=ttc_word_freqs)
# print(pn_ttc_checker.spell("เหลืยม"))
# print(pn_ttc_checker.correct("เหลืยม"))

# # apply different dictionary filter when creating spell checker
# pn_tnc_checker = NorvigSpellChecker()
# print(len(pn_tnc_checker.dictionary()))
# pn_tnc_checker_no_filter = NorvigSpellChecker(dict_filter=None)
# print(len(pn_tnc_checker_no_filter.dictionary()))