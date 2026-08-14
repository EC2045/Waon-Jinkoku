import json
import os

ja = """nav.title=和温陣国
nav.wzn=和温放送局 (WZN)
nav.contact=謁見の間
hero.title=和温陣国
hero.subtitle=State Information Management System
tab.overview=国家概要
tab.culture=文化・歴史
tab.map=国土地図
tab.database=データベース

overview.flag.title=和温陣の旗
overview.flag.desc=デジタルと伝統、そして「安定」の象徴。
overview.entry.title=入国管理システム
overview.entry.desc=ラ＝ウクカ大陸への渡航、および市民権の取得には公式の「入国審査」が必要です。
overview.entry.btn1=入国審査を開始する
overview.entry.btn2=国勢調査に協力する
overview.news.title=Wニュース公式サイト
overview.news.tag=OFFICIAL LINK
overview.news.desc=和温放送局（WZN）による最新の情勢配信。入国前に大陸の現状を確認することを推奨します。

culture.staff.title=王（仮）専用機：和温の杖
culture.staff.heading=和温の杖
culture.staff.desc=この国における「安定」は、杖を介した「陣」の展開によって維持される。国民は各々の役割に基づいた杖を所持し、それは一生の伴侶となる。
culture.staff.note=※王（仮）専用機は、大陸全土の「構造維持」を司る中核デバイスとして、特別なライセンス管理下にあります。
culture.history.title=歴史のアーカイブ
culture.history.btn=📖 歴史書を閲覧 (.txt)

map.title=ラ＝ウクカ大陸全図

footer.title=和温陣国
footer.wzn=WZN-和温放送局
footer.copy=&copy; 2024 Wajin-Tofu Records. All Rights Reserved.

modal.entry.title=大陸入国審査フォーム
modal.entry.name=申請者名
modal.entry.purpose=入国目的
modal.entry.type=所持杖の種類
modal.entry.type.op1=一般用（標準）
modal.entry.type.op2=不安定（魔王領産）
modal.entry.type.op3=未所持
modal.entry.travel=渡航方法
modal.entry.travel.op1=海上（定期船）
modal.entry.travel.op2=陣（空間転移）
modal.entry.check=私は和温陣国の法を遵守し、「安定」を乱さないことを誓います。
modal.entry.submit=申請データを送信

modal.census.title=第1回 和温陣国 国勢調査
modal.census.sub=National Population Census
modal.census.loc=現在の居住地
modal.census.loc.op0=選択してください
modal.census.loc.op1=和陣当府（中央）
modal.census.loc.op2=ラ＝ウクカ境界（緩衝区）
modal.census.loc.op3=不安定の地（旧領）
modal.census.loc.op4=国外 / 渡航中
modal.census.age=年齢層
modal.census.age.op1=20歳未満
modal.census.age.op2=20代〜40代
modal.census.age.op3=40代〜60代
modal.census.age.op4=60歳以上
modal.census.age.op5=不老長寿
modal.census.stab=現在の「安定」度合（自己申告）
modal.census.stab.l=不安定
modal.census.stab.m=中立
modal.census.stab.r=完全安定
modal.census.req=政府への要望・意見
modal.census.submit=回答を正式送信

msg.btn=確認

db.setting.title=和温陣国 基本設定
db.setting.lang_off=公用語：シェルアップ語
db.setting.capital=首都：和陣当府
db.setting.continent=大陸：ラ＝ウクカ大陸
db.setting.lang_use=🌐 使われている言語：<br>【独自言語(互換性がある)】シェルアップ語 / シェランイブ語 / シェランヤブ語<br>【既存言語】英語（古代,現代）/ 日本語（訛りがある、ない場合が多い） / !anbyam ※1

db.food.title=食生活
db.food.desc=刺身、米、カレーなどといった日本文化に影響を受けた食生活。<br>未知の生物でも**「食べられるなら刺身」**という文化がある。<br>そのため、「この生物食える？」ではなく**「刺身にするとどうなる？」**という発想になる。<br>和温陣国固有種も普通に刺身になる。

db.culture.title=文化・技術レベル
db.culture.desc=衛生管理などもしっかりとしているし、ドラゴンの羽を布にしたりする伝統文化がある。<br>また、杖といった未知の技術を有したものもある。これは科学では説明しにくい(できないことはない)が、魔力学という専門の知識が必要である。

db.danger.title=危険度：低
db.danger.desc=「異文化の人であっても安全に暮らすことができる」「衛生管理がしっかりしている」「治安は和温の杖があるため比較的良い」<br>以下の観点から危険性は低いと見られる。<br><br>しかし、**「一部の地域では空間の歪みに巻き込まれる可能性が高い」**ことから、首都の止まるのが良い(首都から出たらどうなるかしらん)。

db.qa.title=Q&A・用語
db.qa.q1=Q. T.Sと絡んだらどうなるのか？
db.qa.a1=A. そもそも関われません。T.Sは和温陣国において「最重要人物」といっても過言ではない人物です。
db.qa.q2=Q. 無理やり関わったら？
db.qa.a2=A. 死にます。また、生き残ったとしても、極刑及び死刑。「複数の異常団体の実験道具になります。」「人型で帰れたら奇跡レベル」
db.qa.q3=Q. T.Sと関わる方法はありますか？
db.qa.a3=A. あります。<br>・和温陣国の政府に許可証を提出し、インタビューを行う<br>・T.S本人に事前に許可をとる(証明する方法も込み)<br>・異常存在に巻き込まれた時(首都内)に異常対策本部に救助され保護される
db.qa.q4=Q. 同一アート作家Rとの関係は？
db.qa.a4=A. よく分かってません。関わったのにも関わらず生きて帰ったのは確かです。
db.qa.q5=Q. 首都以外に行く方法はありますか？
db.qa.a5=A. 許可証を発行してもらえれば、自由に散策することができます。しかし、観光目的で首都以外に行く行為は推奨されません。行くんだったら安全対策をしっかりして、目的を持っていきましょう。
db.qa.q6=Q. 首都以外に行ったらどうなりますか？
db.qa.a6=A. 空間の歪みに巻き込まれる影響は未知数です。運が良ければ壁に埋まるぐらいで済みますが、悪ければ自分が壁になったり、液体になったりします。安全対策はしっかりしてから移動しましょう。
db.qa.q7=Q. onvaの人と関わってもいいの？
db.qa.a7=A. 別に話しても良いですが、onvaのことを聞くのは禁止となっています。<br>理由: onvaが最適化された監視国家だから。

db.glossary.title=用語：ザラヴァサ（zaravasa）
db.glossary.desc=※1 onvaに住んでる人でザラヴァサ（zaravasa）した人が稀に移住している<br><br>**ザラヴァサ（zaravasa） [形]**<br>シェルアップ語が元。最適化されすぎて精神的・肉体的に疲弊した状態。主にonvaから来た移住者が使う表現。

db.chars.title=登録人物・機密データ
db.char1.name=カイ・レノス
db.char1.desc=職業: 外交官 / 言語: シェルアップ語, シェランヤブ語, 日本語 / 種族: 人間
db.char2.name=T.S (仮国籍)
db.char2.desc=職業: 機密事項の観点から非公開 / 種族: 人型生命体 / 年齢: 3i<br>和温陣国の杖を研究、改良する人物。株式会社murinsや記号研究所「架空疑問展」と関わりがある。
db.char3.name=リジェス・アルバルス
db.char3.desc=種族: ウォーウルフ / 年齢: 13<br>名前の通りりっつー・アルバルスと生き別れの弟。T.Sとか関われる力はある。よくわからないポスターを作ってたりもする。
db.char4.name=レイア・ミスト
db.char4.desc=職業: 言語学者・司書 / 言語: シェルアップ語, 古シェルアップ語, 日本語 / 種族: 人間 / 年齢: 23<br>和温陣国中央図書館の管理者。古代シェルアップ語の文献や失われた魔法文字を研究している。
db.char5.name=ノア・ヴェリス
db.char5.desc=職業: 記号工学技師 / 言語: シェルアップ語, シェランヤブ語 / 種族: 人間 / 年齢: 24<br>王立記号工学研究局所属。杖に組み込まれる「記号回路」の設計・開発を担当している。
db.char6.name=エル・サフィア
db.char6.desc=職業: 魔法研究者 / 言語: シェルアップ語, 日本語 / 種族: 人間 / 年齢: 42<br>和温陣国魔法科学院の主任研究員。杖と記号エネルギーの相互作用を専門としている。
db.char7.name=アイリス・フェン
db.char7.desc=職業: 国際分析官 / 言語: シェルアップ語, シェランヤブ語, 日本語, 英語 / 種族: 人間 / 年齢: 19<br>外交省情報分析室所属。各国の文化・言語を調査し、外交官への助言を行う。
db.char8.name=R-09《アルカ》
db.char8.desc=職業: 研究支援AI生命体 / 言語: シェルアップ語, 日本語, 機械言語 / 種族: 人型生命体 / 年齢: NaN<br>T.Sが開発に関わったと噂される人型補助生命体。杖の実験や記号演算の補助を担当するが、開発記録の大部分は非公開。

db.staffs.title=杖の種類
db.staff1.title=テクトニクス
db.staff1.desc=最古の杖にして最高傑作。Y字型の支えがついているのが特徴であり、非常に安定した形状なので、壊れる心配がなく、魔力を簡単に扱うことができる。
db.staff2.title=歴史級の杖（Rekis-Class）
db.staff2.desc=世界の法則そのものに干渉する杖。もしくは、圧倒的な力を持つ杖。<br>例：インテロバング（‽）、数学、核・ウイルス、確定（！）、不定（？）<br>これらは世界を支えるため、通常の杖とは格が違う。しかし現在は故障している。<br><br>**なぜ壊れたのか**<br>世界は歴史級の杖を長期間維持できないことが挙げられる。「歴史級の杖」は、その性質上矛盾や破綻が生み出される。その矛盾や破綻に耐えきれなくなった時、杖は自壊する。<br><br>**残されたもの**<br>杖は壊れたが、設計図、伝承、欠片、神話だけが残っている。だから、「昔は存在した」ことは誰でも知っている。<br><br>現在の王の杖（和温の杖）は歴史級の杖ではない。「国民のまとまり」を尊重する杖である。（日本文化に影響を受けたと思われる）

bd.constitution1.title=和温陣国憲法
db.constitution1.desc=和温陣国は、「安定」と「調律」を国家の礎とし、和温の杖の調和をもって平穏なる秩序を維持する。<br>本国は、杖を生活の基礎インフラとして全市民に保障し、異文化及び未知の価値観に対しても寛容であり続けることを宣言する。<br>




db.history.title=和温陣国史：『‽』から『余白』へ
db.history.1=🌒 黎明と調律の代償<br>東歴850年、「記号」のエネルギーを「杖」で制御する和温陣国が建国された。 しかし、完璧な調律に絶望したある職人が、全てを破壊する「核・ウイルス」の杖を手に魔王と化す。当時の職人たちは、事実を曖昧にする「？」の杖（不定ノ御杖）で魔王を歴史ごと「没案の森」へ封印したが、世界には因果の歪みが残された。
db.history.2=📘 タナトの旅と『‽（インテロバング）』の奇跡<br>時を経て、「らくがき」のような未完成の杖を持つ少年タナトが立ち上がる。彼は世界の基本属性や異国の技術を学び、自らの杖を「テクトニクス」へと進化させた。 4次元の脅威「神の杖」が現れた際、タナトは禁忌である「核・ウイルス」と「？」を解放してこれを撃破。直後に生じた世界の崩壊に対し、職人たちが放った「確定ノ御杖（！）」の光と「？」を合体させ、疑問と確定が共存する「‽（インテロバング）」の杖を創り上げた。<br>全てを「無」に帰そうとした魔王も、タナトの杖の中に自分の苦しみが「世界を構成する不可欠な部品」として調律されているのを見て、自ら「‽」の終止符（ピリオド）へと溶け込み、世界の礎となった。
db.history.3=⚔️ 新たなリーダーと『杖を持たぬ民族』<br>それから5年、大往生を遂げたタナトの跡を継ぎ、青年中下が国のリーダーとなる。 平和な国を揺るがしたのは、島に遭難してきた「杖を使わない民族」との遭遇だった。好戦的な彼らのリーダーに決闘を挑まれた中下は、緑色の杖で風を操り、圧倒的な実力差で相手の巨剣を弾き飛ばす。<br>しかし、勝敗のあとに残ったのは深い問いだった。 「杖は正しすぎる。だから俺たちは、あえて不安定を選んだ」 彼らは無知ゆえに杖を持たないのではなく、和温陣国が選ばなかった「もう一つの解答」として、あえて不確定な未来を生きていたのだ。
db.history.4=🌅 没案庫の余白<br>中下はその出会いを公式記録から抹消し、調律師だけの「没案庫」にそっと書き残した。<br><br>没案記録 No.！？-β「杖を持たないという選択」<br>安定は正義ではない。だが不安定もまた、悪ではない。 世界は“確定された問い”だけでは、前に進めない。<br><br>魔王の熱を内包した「‽」の調律、そして杖を持たぬ者たちの意志。 全てを包み込んだ和温陣国の空で、鮮やかな国旗は、今日も新しく、静かに揺れている。
"""

en = """nav.title=Waon-Jinkoku
nav.wzn=WZN Broadcast
nav.contact=Audience Chamber
hero.title=Waon-Jinkoku
hero.subtitle=State Information Management System
tab.overview=Overview
tab.culture=Culture & History
tab.map=National Map
tab.database=Database

overview.flag.title=Flag of Waon-Jin
overview.flag.desc=A symbol of digital, tradition, and "stability".
overview.entry.title=Immigration System
overview.entry.desc=Travel to the La-Ukuka continent and obtaining citizenship requires an official "Immigration Review".
overview.entry.btn1=Start Immigration Review
overview.entry.btn2=Cooperate with the Census
overview.news.title=W-News Official Site
overview.news.tag=OFFICIAL LINK
overview.news.desc=Latest situation updates by Waon Broadcasting Network (WZN). We recommend checking the continent's current status before entry.

culture.staff.title=King's (Temp) Exclusive Unit: Staff of Waon
culture.staff.heading=Staff of Waon
culture.staff.desc=The "stability" in this country is maintained through the deployment of "formations" via staffs. Citizens possess staffs based on their roles, becoming their lifelong companions.
culture.staff.note=* The King's exclusive unit is under special license management as a core device governing the "structural maintenance" of the entire continent.
culture.history.title=History Archive
culture.history.btn=📖 Read History Book (.txt)

map.title=Complete Map of La-Ukuka Continent

footer.title=Waon-Jinkoku
footer.wzn=WZN-Waon Broadcasting
footer.copy=&copy; 2024 Wajin-Tofu Records. All Rights Reserved.

modal.entry.title=Continental Immigration Review Form
modal.entry.name=Applicant Name
modal.entry.purpose=Purpose of Entry
modal.entry.type=Staff Type Possessed
modal.entry.type.op1=General Use (Standard)
modal.entry.type.op2=Unstable (From Demon Lord's Territory)
modal.entry.type.op3=None
modal.entry.travel=Mode of Travel
modal.entry.travel.op1=Sea (Scheduled Ship)
modal.entry.travel.op2=Formation (Spatial Transfer)
modal.entry.check=I swear to abide by the laws of Waon-Jinkoku and not disturb its "stability".
modal.entry.submit=Submit Application Data

modal.census.title=1st Waon-Jinkoku National Census
modal.census.sub=National Population Census
modal.census.loc=Current Residence
modal.census.loc.op0=Please select
modal.census.loc.op1=Wajin-Tofu (Central)
modal.census.loc.op2=La-Ukuka Boundary (Buffer Zone)
modal.census.loc.op3=Land of Instability (Former Territory)
modal.census.loc.op4=Overseas / In Transit
modal.census.age=Age Group
modal.census.age.op1=Under 20
modal.census.age.op2=20s to 40s
modal.census.age.op3=40s to 60s
modal.census.age.op4=Over 60
modal.census.age.op5=Immortal
modal.census.stab=Current Degree of "Stability" (Self-Reported)
modal.census.stab.l=Unstable
modal.census.stab.m=Neutral
modal.census.stab.r=Fully Stable
modal.census.req=Requests/Opinions to the Government
modal.census.submit=Officially Submit Answers

msg.btn=Confirm

db.setting.title=Waon-Jinkoku Basic Settings
db.setting.lang_off=Official Language: Shell-up
db.setting.capital=Capital: Wajin-Tofu
db.setting.continent=Continent: La-Ukuka
db.setting.lang_use=🌐 Languages Spoken:<br>[Unique Languages (Compatible)] Shell-up / Sheran-ibu / Sheran-yabu<br>[Existing Languages] English (Ancient, Modern) / Japanese (Often without accent) / !anbyam *1

db.food.title=Diet
db.food.desc=A diet influenced by Japanese culture, such as sashimi, rice, and curry.<br>Even with unknown creatures, there is a culture of **"If it's edible, make it sashimi."**<br>Therefore, the question isn't "Can we eat this?" but **"What happens if we make it sashimi?"**<br>Waon-Jinkoku endemic species are also commonly turned into sashimi.

db.culture.title=Cultural and Technological Level
db.culture.desc=Hygiene management is thoroughly established, and there are traditional cultures like using dragon wings as cloth.<br>They also possess unknown technologies such as staffs. While these are hard to explain with science (though not impossible), they require specialized knowledge in magic engineering.

db.danger.title=Danger Level: Low
db.danger.desc="Safe for people of different cultures", "Good hygiene", and "Relatively good public safety due to the Staff of Waon".<br>From these points, the danger level is considered low.<br><br>However, **"some areas have a high possibility of getting caught in spatial distortions,"** so it is better to stay in the capital (who knows what happens if you leave).

db.qa.title=Q&A / Glossary
db.qa.q1=Q. What happens if I interact with T.S?
db.qa.a1=A. You can't in the first place. T.S is arguably the "most important person" in Waon-Jinkoku.
db.qa.q2=Q. What if I force an interaction?
db.qa.a2=A. You die. Even if you survive, extreme penalty and execution. "You'll become an experimental tool for multiple anomalous organizations." "It's a miracle if you return in humanoid form."
db.qa.q3=Q. Is there a way to interact with T.S?
db.qa.a3=A. Yes.<br>- Submit a permit to the government and conduct an interview.<br>- Get prior permission from T.S directly (including proof).<br>- Be rescued and protected by the Anomaly Countermeasure Headquarters when caught in an anomaly (within the capital).
db.qa.q4=Q. What is the relationship with the same art creator R?
db.qa.a4=A. It's not well understood. It's certain that they survived after interacting.
db.qa.q5=Q. Is there a way to go outside the capital?
db.qa.a5=A. With a permit, you can explore freely. However, traveling outside the capital for tourism is not recommended. If you go, take strict safety measures and have a purpose.
db.qa.q6=Q. What happens if I go outside the capital?
db.qa.a6=A. The effects of spatial distortions are unknown. If you're lucky, you might just get stuck in a wall; if unlucky, you might become a wall yourself or turn into liquid. Take strict safety measures.
db.qa.q7=Q. Can I interact with people from onva?
db.qa.a7=A. You can talk to them, but asking about onva is prohibited.<br>Reason: Because onva is a hyper-optimized surveillance state.

db.glossary.title=Glossary: Zaravasa
db.glossary.desc=*1 Rarely, people living in onva who have become zaravasa immigrate here.<br><br>**Zaravasa [Adj]**<br>Derived from Shell-up. A state of mental and physical exhaustion from being too optimized. Mainly used by immigrants from onva.

db.chars.title=Registered Personnel / Classified Data
db.char1.name=Kai Renos
db.char1.desc=Profession: Diplomat / Languages: Shell-up, Sheran-yabu, Japanese / Race: Human
db.char2.name=T.S (Provisional Nationality)
db.char2.desc=Profession: Classified / Race: Humanoid Lifeform / Age: 3i<br>Researches and improves the staffs of Waon-Jinkoku. Connected to murins Inc. and the Semiotics Lab "Fictional Question Exhibition".
db.char3.name=Rigesu Albalusu
db.char3.desc=Race: War Wolf / Age: 13<br>The long-lost younger brother of Ritsu Albalusu. Has the power to interact with T.S. Often makes incomprehensible posters.
db.char4.name=Leia Mist
db.char4.desc=Profession: Linguist & Librarian / Languages: Shell-up, Ancient Shell-up, Japanese / Race: Human / Age: 23<br>Manager of the Waon-Jinkoku Central Library. Researches ancient Shell-up literature and lost magical texts.
db.char5.name=Noa Veris
db.char5.desc=Profession: Symbolic Engineer / Languages: Shell-up, Sheran-yabu / Race: Human / Age: 24<br>Belongs to the Royal Symbolic Engineering Research Bureau. Designs and develops the "symbol circuits" embedded in staffs.
db.char6.name=El Safia
db.char6.desc=Profession: Magic Researcher / Languages: Shell-up, Japanese / Race: Human / Age: 42<br>Chief researcher at the Waon-Jinkoku Academy of Magic Science. Specializes in the interaction between staffs and symbolic energy.
db.char7.name=Iris Fen
db.char7.desc=Profession: International Analyst / Languages: Shell-up, Sheran-yabu, Japanese, English / Race: Human / Age: 19<br>Belongs to the Ministry of Foreign Affairs Intelligence Analysis Office. Investigates foreign cultures and languages to advise diplomats.
db.char8.name=R-09 "Aluka"
db.char8.desc=Profession: Research Support AI Lifeform / Languages: Shell-up, Japanese, Machine Language / Race: Humanoid Lifeform / Age: NaN<br>A humanoid support lifeform rumored to have been co-developed by T.S. Assists in staff experiments and symbolic calculations, but most development logs are classified.

db.staffs.title=Types of Staffs
db.staff1.title=Tectonics
db.staff1.desc=The oldest and greatest staff. Features a Y-shaped support, making it highly stable and immune to breaking, allowing for easy magic handling.
db.staff2.title=Rekis-Class Staff
db.staff2.desc=Staffs that interfere with the laws of the world itself, or possess overwhelming power.<br>Examples: Interrobang (‽), Mathematics, Nuclear/Virus, Confirmation (!), Uncertainty (?)<br>Since these support the world, they are on a different level. However, they are currently broken.<br><br>**Why did they break?**<br>The world cannot sustain Rekis-Class staffs for long periods. Due to their nature, contradictions and collapses occur, causing them to self-destruct when they can no longer bear it.<br><br>**What remains?**<br>The staffs are broken, but blueprints, lore, fragments, and myths remain. Everyone knows "they existed in the past."<br><br>The current King's Staff (Staff of Waon) is not a Rekis-Class. It is a staff that respects "national unity." (Believed to be influenced by Japanese culture)

db.history.title=History of Waon-Jinkoku: From "‽" to "Blank Space"
db.history.1=🌒 Dawn and the Price of Tuning<br>In East Era 850, Waon-Jinkoku was founded to control "Symbol" energy via "Staffs". However, a craftsman who despaired at perfect tuning turned into a Demon Lord with the staffs of "Nuclear and Virus" that destroy everything. The craftsmen of the time sealed him in the "Forest of Rejected Drafts" using the staff of "?" (Staff of Uncertainty) to blur facts, but causal distortions remained in the world.
db.history.2=📘 Tanato's Journey and the Miracle of "‽"<br>Time passed, and a boy named Tanato with an incomplete "doodle"-like staff arose. He learned the world's basic attributes and foreign technologies, evolving his staff into "Tectonics". When the 4D threat "Staff of God" appeared, Tanato released the taboos "Nuclear/Virus" and "?" to defeat it. In response to the subsequent world collapse, he merged the craftsmen's "Staff of Confirmation (!)" with "?", creating the staff of "‽" (Interrobang) where question and certainty coexist.<br>The Demon Lord, seeing his suffering tuned as an "indispensable part of the world" inside Tanato's staff, melted into the period of "‽", becoming the foundation of the world.
db.history.3=⚔️ A New Leader and the "Tribe Without Staffs"<br>Five years later, Tanato passed away, and the young man Nakashita became the leader. The peaceful country was shaken by an encounter with a shipwrecked "Tribe that does not use staffs." Challenged to a duel by their warlike leader, Nakashita manipulated the wind with a green staff, blowing away the giant sword with an overwhelming difference in power.<br>However, what remained was a deep question. "Staffs are too right. That's why we dared to choose instability." They did not lack staffs out of ignorance; they chose an uncertain future as "another answer" that Waon-Jinkoku did not choose.
db.history.4=🌅 The Blank Space in the Rejected Drafts Archive<br>Nakashita erased this encounter from official records, secretly writing it in the tuners' "Rejected Drafts Archive."<br><br>Rejected Draft No. !?-β "The Choice Not to Have a Staff"<br>Stability is not justice. But instability is not evil either. The world cannot move forward with only "confirmed questions".<br><br>The tuning of "‽" containing the Demon Lord's heat, and the will of those without staffs. Wrapped in all this, the vivid flag sways quietly and anew in the Waon-Jinkoku sky today.
"""

eo = """nav.title=Waon-Jinkoku
nav.wzn=WZN-Dissendo
nav.contact=Aŭdienca Ĉambro
hero.title=Waon-Jinkoku
hero.subtitle=Ŝtata Informa Administra Sistemo
tab.overview=Superrigardo
tab.culture=Kulturo & Historio
tab.map=Nacia Mapo
tab.database=Datumbazo

overview.flag.title=Flago de Waon-Jin
overview.flag.desc=Simbolo de cifereca, tradicio, kaj "stabileco".
overview.entry.title=Enmigrada Sistemo
overview.entry.desc=Vojaĝo al la kontinento La-Ukuka kaj akiro de civitaneco postulas oficialan "Enmigradan Revizion".
overview.entry.btn1=Komenci Enmigradan Revizion
overview.entry.btn2=Kunlabori kun la Censo
overview.news.title=W-Novaĵoj Oficiala Retejo
overview.news.tag=OFICIALA LIGILO
overview.news.desc=Plej novaj situaciaj ĝisdatigoj de Waon Broadcasting Network (WZN). Ni rekomendas kontroli la nunan staton de la kontinento antaŭ eniro.

culture.staff.title=Ekskluziva Unuo de Reĝo (Provizora): Bastono de Waon
culture.staff.heading=Bastono de Waon
culture.staff.desc=La "stabileco" en ĉi tiu lando estas konservata per deplojo de "formacioj" per bastonoj. Civitanoj posedas bastonojn bazitajn sur siaj roloj, iĝante iliaj dumvivaj kunuloj.
culture.staff.note=* La ekskluziva unuo de la Reĝo estas sub speciala licenca administrado kiel kerna aparato reganta la "strukturan konservadon" de la tuta kontinento.
culture.history.title=Historia Arkivo
culture.history.btn=📖 Legi Historian Libron (.txt)

map.title=Kompleta Mapo de Kontinento La-Ukuka

footer.title=Waon-Jinkoku
footer.wzn=WZN-Waon-Dissendo
footer.copy=&copy; 2024 Wajin-Tofu Records. Ĉiuj Rajtoj Rezervitaj.

modal.entry.title=Kontinenta Enmigrada Revizia Formularo
modal.entry.name=Nomo de Kandidato
modal.entry.purpose=Celo de Eniro
modal.entry.type=Speco de Posedata Bastono
modal.entry.type.op1=Ĝenerala Uzo (Norma)
modal.entry.type.op2=Malstabila (De Teritorio de Demona Sinjoro)
modal.entry.type.op3=Neniu
modal.entry.travel=Vojaĝmaniero
modal.entry.travel.op1=Maro (Planita Ŝipo)
modal.entry.travel.op2=Formacio (Spaca Translokigo)
modal.entry.check=Mi ĵuras obei la leĝojn de Waon-Jinkoku kaj ne ĝeni ĝian "stabilecon".
modal.entry.submit=Afiŝi Aplikajn Datumojn

modal.census.title=1-a Nacia Censo de Waon-Jinkoku
modal.census.sub=Nacia Loĝantara Censo
modal.census.loc=Nuna Loĝloko
modal.census.loc.op0=Bonvolu elekti
modal.census.loc.op1=Wajin-Tofu (Centra)
modal.census.loc.op2=Limo de La-Ukuka (Bufrozono)
modal.census.loc.op3=Lando de Malstabileco (Iama Teritorio)
modal.census.loc.op4=Eksterlande / En Transiro
modal.census.age=Aĝoklaso
modal.census.age.op1=Sub 20
modal.census.age.op2=20-aj ĝis 40-aj jaroj
modal.census.age.op3=40-aj ĝis 60-aj jaroj
modal.census.age.op4=Super 60
modal.census.age.op5=Senmorta
modal.census.stab=Nuna Grado de "Stabileco" (Memraportita)
modal.census.stab.l=Malstabila
modal.census.stab.m=Neŭtrala
modal.census.stab.r=Plene Stabila
modal.census.req=Petoj/Opinioj al la Registaro
modal.census.submit=Oficiale Sendi Respondojn

msg.btn=Konfirmi

db.setting.title=Bazaj Agordoj de Waon-Jinkoku
db.setting.lang_off=Oficiala Lingvo: Ŝel-up
db.setting.capital=Ĉefurbo: Wajin-Tofu
db.setting.continent=Kontinento: La-Ukuka
db.setting.lang_use=🌐 Parolataj Lingvoj:<br>[Unikaj Lingvoj (Kongruaj)] Ŝel-up / Ŝeran-ibu / Ŝeran-yabu<br>[Ekzistantaj Lingvoj] Angla (Antikva, Moderna) / Japana (Ofte sen akĉento) / !anbyam *1

db.food.title=Dieto
db.food.desc=Dieto influita de la japana kulturo, kiel saŝimio, rizo, kaj kareo.<br>Eĉ ĉe nekonataj estaĵoj, ekzistas kulturo de **"Se ĝi estas manĝebla, faru ĝin saŝimio."**<br>Sekve, la demando ne estas "Ĉu ni povas manĝi ĉi tion?" sed **"Kio okazas se ni faras ĝin saŝimio?"**<br>Endemiaj specioj de Waon-Jinkoku ankaŭ kutime fariĝas saŝimio.

db.culture.title=Kultura kaj Teknologia Nivelo
db.culture.desc=Higiena administrado estas plene establita, kaj ekzistas tradiciaj kulturoj kiel uzi drakflugilojn kiel ŝtofon.<br>Ili ankaŭ posedas nekonatajn teknologiojn kiel bastonojn. Kvankam ĉi tiuj malfacilas klarigi per scienco (kvankam ne neeble), ili postulas specialan scion pri magia inĝenierado.

db.danger.title=Nivelo de Danĝero: Malalta
db.danger.desc="Sekura por homoj de diversaj kulturoj", "Bona higieno", kaj "Relative bona publika sekureco pro la Bastono de Waon".<br>El ĉi tiuj punktoj, la nivelo de danĝero estas konsiderata malalta.<br><br>Tamen, **"iuj areoj havas altan eblecon esti kaptitaj en spacaj distordoj,"** do estas pli bone resti en la ĉefurbo (kiu scias, kio okazas se vi eliras).

db.qa.title=Q&A / Glosaro
db.qa.q1=Q. Kio okazas se mi interagas kun T.S?
db.qa.a1=A. Vi unue ne povas. T.S estas eble la "plej grava persono" en Waon-Jinkoku.
db.qa.q2=Q. Kio se mi devigas interagadon?
db.qa.a2=A. Vi mortas. Eĉ se vi postvivas, ekstrema puno kaj ekzekuto. "Vi fariĝos eksperimenta ilo por multoblaj anomaliaj organizaĵoj." "Estas miraklo se vi revenos en homoida formo."
db.qa.q3=Q. Ĉu ekzistas maniero interagi kun T.S?
db.qa.a3=A. Jes.<br>- Submetu permesilon al la registaro kaj faru intervjuon.<br>- Akiru antaŭan permeson de T.S rekte (inkluzive de pruvo).<br>- Estu savita kaj protektita de la Kontraŭanomalia Ĉefstabejo kiam vi estas kaptita en anomaliom (ene de la ĉefurbo).
db.qa.q4=Q. Kio estas la rilato kun la sama artokreinto R?
db.qa.a4=A. Ĝi ne estas bone komprenita. Estas certe ke ili postvivis post interagado.
db.qa.q5=Q. Ĉu ekzistas maniero iri ekster la ĉefurbo?
db.qa.a5=A. Kun permesilo, vi povas esplori libere. Tamen, vojaĝi ekster la ĉefurbo por turismo ne estas rekomendita. Se vi iras, prenu striktajn sekurecajn mezurojn kaj havu celon.
db.qa.q6=Q. Kio okazas se mi iras ekster la ĉefurbo?
db.qa.a6=A. La efikoj de spacaj distordoj estas nekonataj. Se vi havas bonŝancon, vi eble nur blokos en muro; se malbonŝancon, vi eble fariĝos muro mem aŭ iĝos likvaĵo. Prenu striktajn sekurecajn mezurojn.
db.qa.q7=Q. Ĉu mi povas interagi kun homoj de onva?
db.qa.a7=A. Vi povas paroli kun ili, sed demandi pri onva estas malpermesita.<br>Kialo: Ĉar onva estas hiperoptimumigita kontrolŝtato.

db.glossary.title=Glosaro: Zaravasa
db.glossary.desc=*1 Malofte, homoj vivantaj en onva, kiuj fariĝis zaravasa, enmigras ĉi tien.<br><br>**Zaravasa [Adj]**<br>Derivita de Ŝel-up. Stato de mensa kaj fizika elĉerpiĝo pro troa optimumigo. Ĉefe uzata de enmigrintoj de onva.

db.chars.title=Registrita Personaro / Klasigita Datumo
db.char1.name=Kai Renos
db.char1.desc=Profesio: Diplomato / Lingvoj: Ŝel-up, Ŝeran-yabu, Japana / Raso: Homo
db.char2.name=T.S (Provizora Nacieco)
db.char2.desc=Profesio: Klasigita / Raso: Homoida Vivoformo / Aĝo: 3i<br>Esploras kaj plibonigas la bastonojn de Waon-Jinkoku. Ligita al murins Inc. kaj la Semiotika Laboratorio "Fikcia Demanda Ekspozicio".
db.char3.name=Rigesu Albalusu
db.char3.desc=Raso: Milita Lupo / Aĝo: 13<br>La longe perdita pli juna frato de Ritsu Albalusu. Havas la potencon interagi kun T.S. Ofte faras nekompreneblajn afiŝojn.
db.char4.name=Leia Mist
db.char4.desc=Profesio: Lingvisto & Bibliotekisto / Lingvoj: Ŝel-up, Antikva Ŝel-up, Japana / Raso: Homo / Aĝo: 23<br>Manaĝero de la Centra Biblioteko Waon-Jinkoku. Esploras antikvan literaturon Ŝel-up kaj perditajn magiajn tekstojn.
db.char5.name=Noa Veris
db.char5.desc=Profesio: Simbola Inĝeniero / Lingvoj: Ŝel-up, Ŝeran-yabu / Raso: Homo / Aĝo: 24<br>Apertenas al la Reĝa Simbola Inĝenieria Esplora Buroo. Dezajnas kaj disvolvas la "simbolajn cirkvitojn" enkonstruitajn en bastonojn.
db.char6.name=El Safia
db.char6.desc=Profesio: Magia Esploristo / Lingvoj: Ŝel-up, Japana / Raso: Homo / Aĝo: 42<br>Ĉefa esploristo ĉe la Akademio de Magia Scienco de Waon-Jinkoku. Specialiĝas pri la interago inter bastonoj kaj simbola energio.
db.char7.name=Iris Fen
db.char7.desc=Profesio: Internacia Analizisto / Lingvoj: Ŝel-up, Ŝeran-yabu, Japana, Angla / Raso: Homo / Aĝo: 19<br>Apertenas al la Oficejo pri Inteligenta Analizo de la Ministerio de Eksterlandaj Aferoj. Esploras eksterlandajn kulturojn kaj lingvojn por konsili diplomatojn.
db.char8.name=R-09 "Aluka"
db.char8.desc=Profesio: Esplora Subtena AI-Vivoformo / Lingvoj: Ŝel-up, Japana, Maŝina Lingvo / Raso: Homoida Vivoformo / Aĝo: NaN<br>Homoida subtena vivoformo disvastigita esti kun-disvolvita de T.S. Asistas en bastonaj eksperimentoj kaj simbolaj kalkuloj, sed plej multaj disvolvaj protokoloj estas klasigitaj.

db.staffs.title=Specoj de Bastonoj
db.staff1.title=Tectonics
db.staff1.desc=La plej malnova kaj plej bonega bastono. Havas Y-forman subtenon, igante ĝin tre stabila kaj imuna al rompiĝo, permesante facilan magian manipuladon.
db.staff2.title=Rekis-Klasa Bastono
db.staff2.desc=Bastonoj, kiuj interferas kun la leĝoj de la mondo mem, aŭ posedas superfortan potencon.<br>Ekzemploj: Interrobang (‽), Matematiko, Nuklea/Viruso, Konfirmo (!), Necerteco (?)<br>Ĉar ĉi tiuj subtenas la mondon, ili estas sur alia nivelo. Tamen, ili nuntempe estas rompitaj.<br><br>**Kial ili rompiĝis?**<br>La mondo ne povas subteni Rekis-Klasajn bastonojn dum longaj periodoj. Pro ilia naturo, kontraŭdiroj kaj kolapsoj okazas, kaŭzante ilin memdetruiĝi kiam ili ne plu povas elteni.<br><br>**Kio restas?**<br>La bastonoj estas rompitaj, sed blukopioj, tradicioj, fragmentoj, kaj mitoj restas. Ĉiuj scias "ili ekzistis en la pasinteco."<br><br>La nuna Bastono de la Reĝo (Bastono de Waon) ne estas Rekis-Klasa. Ĝi estas bastono, kiu respektas "nacian unuecon." (Kredita esti influita de la japana kulturo)

db.history.title=Historio de Waon-Jinkoku: De "‽" ĝis "Blanka Spaco"
db.history.1=🌒 Tagiĝo kaj la Prezo de Agordado<br>En Orienta Epoko 850, Waon-Jinkoku estis fondita por kontroli "Simbolan" energion per "Bastonoj". Tamen, metiisto, kiu malesperis pro perfekta agordado, fariĝis Demona Sinjoro kun la bastonoj de "Nuklea kaj Viruso", kiuj detruas ĉion. La metiistoj de la tempo sigelis lin en la "Arbaro de Malakceptitaj Skizoj" uzante la bastonon de "?" (Bastono de Necerteco) por malklarigi faktojn, sed kaŭzaj distordoj restis en la mondo.
db.history.2=📘 La Vojaĝo de Tanato kaj la Miraklo de "‽"<br>Tempo pasis, kaj knabo nomita Tanato kun nekompleta "skribaĉa"-simila bastono ekstaris. Li lernis la bazajn atributojn de la mondo kaj eksterlandajn teknologiojn, evoluigante sian bastonon en "Tectonics". Kiam la 4D minaco "Bastono de Dio" aperis, Tanato liberigis la tabuojn "Nuklea/Viruso" kaj "?" por venki ĝin. Responde al la posta monda kolapso, li kunfandis la "Bastonon de Konfirmo (!)" de la metiistoj kun "?", kreante la bastonon de "‽" (Interrobang) kie demando kaj certeco kunekzistas.<br>La Demona Sinjoro, vidante sian suferon agorditan kiel "necesa parto de la mondo" ene de la bastono de Tanato, fandiĝis en la punkton de "‽", iĝante la fundamento de la mondo.
db.history.3=⚔️ Nova Gvidanto kaj la "Tribo Sen Bastonoj"<br>Kvin jarojn poste, Tanato mortis, kaj la juna viro Nakashita fariĝis la gvidanto. La paca lando estis skuita per renkonto kun ŝippereinta "Tribo, kiu ne uzas bastonojn." Defiita al duelo fare de ilia militema gvidanto, Nakashita manipulis la venton per verda bastono, forblovante la gigantan glavon per superforta diferenco en potenco.<br>Tamen, kio restis estis profunda demando. "Bastonoj estas tro pravaj. Tial ni kuraĝis elekti malstabilecon." Al ili ne mankis bastonoj pro nescio; ili elektis necertan estontecon kiel "alian respondon", kiun Waon-Jinkoku ne elektis.
db.history.4=🌅 La Blanka Spaco en la Arkivo de Malakceptitaj Skizoj<br>Nakashita forigis ĉi tiun renkonton el oficialaj registroj, sekrete skribante ĝin en la "Arkivo de Malakceptitaj Skizoj" de la agordantoj.<br><br>Malakceptita Skizo N-ro !?-β "La Elekto Ne Havi Bastonon"<br>Stabileco ne estas justeco. Sed malstabileco ankaŭ ne estas malbono. La mondo ne povas antaŭeniri nur kun "konfirmitaj demandoj".<br><br>La agordado de "‽" enhavanta la varmon de la Demona Sinjoro, kaj la volo de tiuj sen bastonoj. Envolvita en ĉio ĉi, la vigla flago svingiĝas trankvile kaj denove en la ĉielo de Waon-Jinkoku hodiaŭ.
"""

with open("/Users/rituto/Documents/GitHub/Waon-Jinkoku/ja.lang", "w") as f:
    f.write(ja)
with open("/Users/rituto/Documents/GitHub/Waon-Jinkoku/en.lang", "w") as f:
    f.write(en)
with open("/Users/rituto/Documents/GitHub/Waon-Jinkoku/eo.lang", "w") as f:
    f.write(eo)
