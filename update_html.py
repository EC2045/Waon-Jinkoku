html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title data-lang-key="nav.title">和温陣国 公式サイト</title>
    <link rel="icon" href="icon.png" />
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700&family=DotGothic16&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="src/style_44d90307.css">
    <script src="../scripts/font.js" data-lang-path="{lang}.lang"></script>
</head>
<body>

    <!-- ナビゲーション -->
    <nav class="fixed w-full z-50 bg-black/90 border-b border-white/10 px-6 py-4 flex justify-between items-center backdrop-blur-md">
        <div class="text-2xl font-bold tracking-widest pixel-font flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-gradient-to-b from-red-600 to-blue-700 shadow-[0_0_10px_rgba(255,0,0,0.3)]"></div>
            <span data-lang-key="nav.title">和温陣国</span>
        </div>
        <div class="hidden md:flex space-x-6 text-xs uppercase tracking-widest items-center">
            <a href="https://ec2045.github.io/WZN/" target="_blank" class="flex items-center gap-2 text-yellow-500 hover:text-yellow-400 transition bg-yellow-500/10 px-3 py-1 rounded border border-yellow-500/20">
                <span class="relative flex h-2 w-2">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-yellow-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2 bg-yellow-500"></span>
                </span>
                <span data-lang-key="nav.wzn">和温放送局 (WZN)</span>
            </a>
            <a href="#contact" class="hover:text-red-500 transition" data-lang-key="nav.contact">謁見の間</a>
        </div>
    </nav>

    <!-- ヒーロー -->
    <section class="hero-section">
        <img src="旗.png" alt="和温陣国の旗" class="hero-bg-image">
        <div class="text-center z-10 px-4 mt-12">
            <h1 class="text-5xl md:text-7xl font-bold mb-4 pixel-font drop-shadow-lg text-white" data-lang-key="hero.title">和温陣国</h1>
            <p class="text-zinc-500 tracking-[0.4em] text-sm uppercase pixel-font" data-lang-key="hero.subtitle">State Information Management System</p>
        </div>
    </section>

    <!-- タブナビ -->
    <div class="sticky top-[73px] z-40 bg-black border-b border-white/10">
        <div class="max-w-6xl mx-auto flex justify-center overflow-x-auto">
            <button onclick="switchTab('tab-overview')" id="btn-tab-overview" class="tab-btn active pixel-font text-xs md:text-sm uppercase whitespace-nowrap" data-lang-key="tab.overview">国家概要</button>
            <button onclick="switchTab('tab-culture')" id="btn-tab-culture" class="tab-btn pixel-font text-xs md:text-sm uppercase whitespace-nowrap" data-lang-key="tab.culture">文化・歴史</button>
            <button onclick="switchTab('tab-map')" id="btn-tab-map" class="tab-btn pixel-font text-xs md:text-sm uppercase whitespace-nowrap" data-lang-key="tab.map">国土地図</button>
            <button onclick="switchTab('tab-database')" id="btn-tab-database" class="tab-btn pixel-font text-xs md:text-sm uppercase whitespace-nowrap text-red-500" data-lang-key="tab.database">データベース</button>
        </div>
    </div>

    <!-- コンテンツ -->
    <main class="max-w-6xl mx-auto py-12 px-6 min-h-screen">
        
        <!-- 国家概要 -->
        <div id="tab-overview" class="tab-content active">
            <div class="grid md:grid-cols-2 gap-12 items-start">
                <div class="space-y-8">
                    <div class="border-l-4 border-red-600 pl-6">
                        <h2 class="text-3xl font-bold mb-4 pixel-font italic" data-lang-key="overview.flag.title">和温陣の旗</h2>
                        <p class="text-gray-400 leading-relaxed" data-lang-key="overview.flag.desc">デジタルと伝統、そして「安定」の象徴。</p>
                    </div>
                    <img src="旗.png" alt="国旗" class="w-full border border-white/10 shadow-2xl">
                </div>
                <div class="space-y-6">
                    <!-- 入国管理システムカード -->
                    <div class="card p-8 border-l-2 border-red-600">
                        <h3 class="text-xl font-bold mb-4 pixel-font italic text-red-500" data-lang-key="overview.entry.title">入国管理システム</h3>
                        <p class="text-sm text-zinc-400 mb-6" data-lang-key="overview.entry.desc">ラ＝ウクカ大陸への渡航、および市民権の取得には公式の「入国審査」が必要です。</p>
                        <div class="flex flex-col gap-4">
                            <button onclick="openModal('entryModal')" class="w-full bg-red-600 text-white py-4 font-bold hover:bg-red-700 transition pixel-font shadow-lg" data-lang-key="overview.entry.btn1">入国審査を開始する</button>
                            <button onclick="openModal('censusModal')" class="w-full border border-white/20 py-3 font-bold hover:bg-zinc-800 transition pixel-font text-sm" data-lang-key="overview.entry.btn2">国勢調査に協力する</button>
                        </div>
                    </div>

                    <!-- Wニュースサイトカード -->
                    <a href="https://ec2045.github.io/WZN/" target="_blank" class="news-card block p-6 rounded relative overflow-hidden group">
                        <div class="flex items-center justify-between mb-3">
                            <h3 class="text-xl font-bold pixel-font text-yellow-500 flex items-center gap-2">
                                <span class="block w-2 h-2 bg-yellow-500 animate-pulse rounded-full"></span>
                                <span data-lang-key="overview.news.title">Wニュース公式サイト</span>
                            </h3>
                            <span class="text-[10px] text-yellow-600 border border-yellow-900 px-2 py-0.5 rounded" data-lang-key="overview.news.tag">OFFICIAL LINK</span>
                        </div>
                        <p class="text-xs text-zinc-400 leading-relaxed group-hover:text-zinc-200 transition" data-lang-key="overview.news.desc">
                            和温放送局（WZN）による最新の情勢配信。入国前に大陸の現状を確認することを推奨します。
                        </p>
                        <div class="mt-4 flex justify-end">
                            <span class="text-[10px] pixel-font text-yellow-500 opacity-50 group-hover:opacity-100 transition">EXTERNAL_SITE >></span>
                        </div>
                    </a>
                </div>
            </div>
        </div>

        <!-- 文化・歴史 -->
        <div id="tab-culture" class="tab-content">
            <div class="space-y-16">
                <section class="grid md:grid-cols-2 gap-12 items-center">
                    <div class="space-y-6">
                        <div class="p-6 bg-yellow-500/5 border border-yellow-500/20 rounded">
                            <img src="和温の杖.png" alt="和温の杖" class="h-24 mx-auto mb-4 drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                            <p class="text-xs text-center text-yellow-500 font-bold pixel-font" data-lang-key="culture.staff.title">王（仮）専用機：和温の杖</p>
                        </div>
                        <img src="杖.png" alt="杖の文化" class="w-full border border-white/5 rounded shadow-lg">
                    </div>
                    
                    <div>
                        <h2 class="text-3xl font-bold mb-6 pixel-font" data-lang-key="culture.staff.heading">和温の杖</h2>
                        <p class="text-gray-300 leading-relaxed mb-6" data-lang-key="culture.staff.desc">
                            この国における「安定」は、杖を介した「陣」の展開によって維持される。国民は各々の役割に基づいた杖を所持し、それは一生の伴侶となる。
                        </p>
                        <div class="p-4 border-l-2 border-zinc-700 bg-zinc-900/40">
                            <p class="text-xs text-zinc-500 italic" data-lang-key="culture.staff.note">
                                ※王（仮）専用機は、大陸全土の「構造維持」を司る中核デバイスとして、特別なライセンス管理下にあります。
                            </p>
                        </div>
                    </div>
                </section>
                <div class="text-center py-12 border-y border-white/5 bg-zinc-900/20">
                    <h3 class="text-2xl font-bold mb-6 pixel-font" data-lang-key="culture.history.title">歴史のアーカイブ</h3>
                    <a href="history.txt" download="history.txt" class="bg-white text-black px-10 py-4 font-bold hover:bg-red-600 hover:text-white transition pixel-font inline-flex items-center gap-3" data-lang-key="culture.history.btn">
                        📖 歴史書を閲覧 (.txt)
                    </a>
                </div>
            </div>
        </div>

        <!-- 地図 -->
        <div id="tab-map" class="tab-content">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-3xl font-bold mb-8 pixel-font text-center" data-lang-key="map.title">ラ＝ウクカ大陸全図</h2>
                <div class="map-container rounded shadow-2xl">
                    <img src="map.png" alt="地図" class="map-image">
                    <div class="absolute top-4 left-4 bg-black/80 px-3 py-1 border border-white/10 text-[10px] pixel-font">MAP_ID: LA-UKUKA_01</div>
                </div>
            </div>
        </div>

        <!-- データベース（新規追加） -->
        <div id="tab-database" class="tab-content">
            <div class="space-y-12">
                <!-- 基本設定 -->
                <section class="card p-8 border-l-4 border-red-600 bg-zinc-900/80">
                    <h2 class="text-2xl font-bold mb-6 pixel-font text-red-500" data-lang-key="db.setting.title">和温陣国 基本設定</h2>
                    <div class="grid md:grid-cols-3 gap-4 mb-6 text-sm">
                        <div class="bg-black/50 p-4 rounded border border-white/10" data-lang-key="db.setting.lang_off">公用語：シェルアップ語</div>
                        <div class="bg-black/50 p-4 rounded border border-white/10" data-lang-key="db.setting.capital">首都：和陣当府</div>
                        <div class="bg-black/50 p-4 rounded border border-white/10" data-lang-key="db.setting.continent">大陸：ラ＝ウクカ大陸</div>
                    </div>
                    <div class="text-sm text-zinc-300 leading-relaxed bg-black/40 p-4 rounded border border-white/5" data-lang-key="db.setting.lang_use">
                        🌐 使われている言語：<br>【独自言語(互換性がある)】シェルアップ語 / シェランイブ語 / シェランヤブ語<br>【既存言語】英語（古代,現代）/ 日本語（訛りがある、ない場合が多い） / !anbyam ※1
                    </div>
                </section>

                <!-- 食生活・文化・危険度 -->
                <div class="grid md:grid-cols-3 gap-6">
                    <div class="card p-6 border-t-2 border-yellow-500 bg-zinc-900/60">
                        <h3 class="text-lg font-bold mb-3 pixel-font text-yellow-500" data-lang-key="db.food.title">食生活</h3>
                        <div class="text-xs text-zinc-400 leading-relaxed space-y-2" data-lang-key="db.food.desc">
                            刺身、米、カレーなどといった日本文化に影響を受けた食生活。<br>未知の生物でも「食べられるなら刺身」という文化がある。<br>そのため、「この生物食える？」ではなく「刺身にするとどうなる？」という発想になる。<br>和温陣国固有種も普通に刺身になる。
                        </div>
                    </div>
                    <div class="card p-6 border-t-2 border-blue-500 bg-zinc-900/60">
                        <h3 class="text-lg font-bold mb-3 pixel-font text-blue-500" data-lang-key="db.culture.title">文化・技術レベル</h3>
                        <div class="text-xs text-zinc-400 leading-relaxed space-y-2" data-lang-key="db.culture.desc">
                            衛生管理などもしっかりとしているし、ドラゴンの羽を布にしたりする伝統文化がある。<br>また、杖といった未知の技術を有したものもある。これは科学では説明しにくい(できないことはない)が、魔力学という専門の知識が必要である。
                        </div>
                    </div>
                    <div class="card p-6 border-t-2 border-green-500 bg-zinc-900/60">
                        <h3 class="text-lg font-bold mb-3 pixel-font text-green-500" data-lang-key="db.danger.title">危険度：低</h3>
                        <div class="text-xs text-zinc-400 leading-relaxed space-y-2" data-lang-key="db.danger.desc">
                            「異文化の人であっても安全に暮らすことができる」「衛生管理がしっかりしている」「治安は和温の杖があるため比較的良い」<br>以下の観点から危険性は低いと見られる。<br><br>しかし、「一部の地域では空間の歪みに巻き込まれる可能性が高い」ことから、首都の止まるのが良い(首都から出たらどうなるかしらん)。
                        </div>
                    </div>
                </div>

                <!-- 登録人物 -->
                <section class="space-y-6">
                    <h2 class="text-2xl font-bold pixel-font border-l-4 border-red-600 pl-4" data-lang-key="db.chars.title">登録人物・機密データ</h2>
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="card p-5 bg-zinc-900/90 border border-white/10">
                            <h4 class="text-md font-bold pixel-font text-red-400 mb-1" data-lang-key="db.char1.name">カイ・レノス</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char1.desc">職業: 外交官 / 言語: シェルアップ語, シェランヤブ語, 日本語 / 種族: 人間</p>
                        </div>
                        <div class="card p-5 bg-zinc-900/90 border border-red-500/30">
                            <h4 class="text-md font-bold pixel-font text-yellow-400 mb-1" data-lang-key="db.char2.name">T.S (仮国籍)</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char2.desc">職業: 機密事項の観点から非公開 / 種族: 人型生命体 / 年齢: 3i<br>和温陣国の杖を研究、改良する人物。株式会社murinsや記号研究所「架空疑問展」と関わりがある。</p>
                        </div>
                        <div class="card p-5 bg-zinc-900/90 border border-white/10">
                            <h4 class="text-md font-bold pixel-font text-red-400 mb-1" data-lang-key="db.char3.name">リジェス・アルバルス</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char3.desc">種族: ウォーウルフ / 年齢: 13<br>名前の通りりっつー・アルバルスと生き別れの弟。T.Sとか関われる力はある。よくわからないポスターを作ってたりもする。</p>
                        </div>
                        <div class="card p-5 bg-zinc-900/90 border border-white/10">
                            <h4 class="text-md font-bold pixel-font text-red-400 mb-1" data-lang-key="db.char4.name">レイア・ミスト</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char4.desc">職業: 言語学者・司書 / 言語: シェルアップ語, 古シェルアップ語, 日本語 / 種族: 人間 / 年齢: 23<br>和温陣国中央図書館の管理者。古代シェルアップ語の文献や失われた魔法文字を研究している。</p>
                        </div>
                        <div class="card p-5 bg-zinc-900/90 border border-white/10">
                            <h4 class="text-md font-bold pixel-font text-red-400 mb-1" data-lang-key="db.char5.name">ノア・ヴェリス</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char5.desc">職業: 記号工学技師 / 言語: シェルアップ語, シェランヤブ語 / 種族: 人間 / 年齢: 24<br>王立記号工学研究局所属。杖に組み込まれる「記号回路」の設計・開発を担当している。</p>
                        </div>
                        <div class="card p-5 bg-zinc-900/90 border border-white/10">
                            <h4 class="text-md font-bold pixel-font text-red-400 mb-1" data-lang-key="db.char6.name">エル・サフィア</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char6.desc">職業: 魔法研究者 / 言語: シェルアップ語, 日本語 / 種族: 人間 / 年齢: 42<br>和温陣国魔法科学院の主任研究員。杖と記号エネルギーの相互作用を専門としている。</p>
                        </div>
                        <div class="card p-5 bg-zinc-900/90 border border-white/10">
                            <h4 class="text-md font-bold pixel-font text-red-400 mb-1" data-lang-key="db.char7.name">アイリス・フェン</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char7.desc">職業: 国際分析官 / 言語: シェルアップ語, シェランヤブ語, 日本語, 英語 / 種族: 人間 / 年齢: 19<br>外交省情報分析室所属。各国の文化・言語を調査し、外交官への助言を行う。</p>
                        </div>
                        <div class="card p-5 bg-zinc-900/90 border border-white/10">
                            <h4 class="text-md font-bold pixel-font text-red-400 mb-1" data-lang-key="db.char8.name">R-09《アルカ》</h4>
                            <p class="text-xs text-zinc-400" data-lang-key="db.char8.desc">職業: 研究支援AI生命体 / 言語: シェルアップ語, 日本語, 機械言語 / 種族: 人型生命体 / 年齢: NaN<br>T.Sが開発に関わったと噂される人型補助生命体。杖の実験や記号演算の補助を担当するが、開発記録の大部分は非公開。</p>
                        </div>
                    </div>
                </section>

                <!-- 杖の種類 -->
                <section class="space-y-6">
                    <h2 class="text-2xl font-bold pixel-font border-l-4 border-yellow-500 pl-4" data-lang-key="db.staffs.title">杖の種類</h2>
                    <div class="space-y-4">
                        <div class="card p-6 bg-zinc-900/90 border border-yellow-500/30">
                            <h3 class="text-lg font-bold pixel-font text-yellow-500 mb-2" data-lang-key="db.staff1.title">テクトニクス</h3>
                            <p class="text-xs text-zinc-300 leading-relaxed" data-lang-key="db.staff1.desc">最古の杖にして最高傑作。Y字型の支えがついているのが特徴であり、非常に安定した形状なので、壊れる心配がなく、魔力を簡単に扱うことができる。</p>
                        </div>
                        <div class="card p-6 bg-zinc-900/90 border border-red-500/30">
                            <h3 class="text-lg font-bold pixel-font text-red-500 mb-2" data-lang-key="db.staff2.title">歴史級の杖（Rekis-Class）</h3>
                            <div class="text-xs text-zinc-300 leading-relaxed space-y-3" data-lang-key="db.staff2.desc">
                                世界の法則そのものに干渉する杖。もしくは、圧倒的な力を持つ杖。<br>例：インテロバング（‽）、数学、核・ウイルス、確定（！）、不定（？）<br>これらは世界を支えるため、通常の杖とは格が違う。しかし現在は故障している。<br><br><b>なぜ壊れたのか</b><br>世界は歴史級の杖を長期間維持できないことが挙げられる。「歴史級の杖」は、その性質上矛盾や破綻が生み出される。その矛盾や破綻に耐えきれなくなった時、杖は自壊する。<br><br><b>残されたもの</b><br>杖は壊れたが、設計図、伝承、欠片、神話だけが残っている。だから、「昔は存在した」ことは誰でも知っている。<br><br>現在の王の杖（和温の杖）は歴史級の杖ではない。「国民のまとまり」を尊重する杖である。（日本文化に影響を受けたと思われる）
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 歴史編 -->
                <section class="space-y-6">
                    <h2 class="text-2xl font-bold pixel-font border-l-4 border-blue-500 pl-4" data-lang-key="db.history.title">和温陣国史：『‽』から『余白』へ</h2>
                    <div class="space-y-4 text-xs text-zinc-300 leading-relaxed bg-zinc-900/90 p-6 rounded border border-white/10">
                        <div class="p-3 bg-black/40 rounded" data-lang-key="db.history.1">🌒 黎明と調律の代償<br>東歴850年、「記号」のエネルギーを「杖」で制御する和温陣国が建国された。 しかし、完璧な調律に絶望したある職人が、全てを破壊する「核・ウイルス」の杖を手に魔王と化す。当時の職人たちは、事実を曖昧にする「？」の杖（不定ノ御杖）で魔王を歴史ごと「没案の森」へ封印したが、世界には因果の歪みが残された。</div>
                        <div class="p-3 bg-black/40 rounded" data-lang-key="db.history.2">📘 タナトの旅と『‽（インテロバング）』の奇跡<br>時を経て、「らくがき」のような未完成の杖を持つ少年タナトが立ち上がる。彼は世界の基本属性や異国の技術を学び、自らの杖を「テクトニクス」へと進化させた。 4次元の脅威「神の杖」が現れた際、タナトは禁忌である「核・ウイルス」と「？」を解放してこれを撃破。直後に生じた世界の崩壊に対し、職人たちが放った「確定ノ御杖（！）」の光と「？」を合体させ、疑問と確定が共存する「‽（インテロバング）」の杖を創り上げた。<br>全てを「無」に帰そうとした魔王も、タナトの杖の中に自分の苦しみが「世界を構成する不可欠な部品」として調律されているのを見て、自ら「‽」の終止符（ピリオド）へと溶け込み、世界の礎となった。</div>
                        <div class="p-3 bg-black/40 rounded" data-lang-key="db.history.3">⚔️ 新たなリーダーと『杖を持たぬ民族』<br>それから5年、大往生を遂げたタナトの跡を継ぎ、青年中下が国のリーダーとなる。 平和な国を揺るがしたのは、島に遭難してきた「杖を使わない民族」との遭遇だった。好戦的な彼らのリーダーに決闘を挑まれた中下は、緑色の杖で風を操り、圧倒的な実力差で相手の巨剣を弾き飛ばす。<br>しかし、勝敗のあとに残ったのは深い問いだった。 「杖は正しすぎる。だから俺たちは、あえて不安定を選んだ」 彼らは無知ゆえに杖を持たないのではなく、和温陣国が選ばなかった「もう一つの解答」として、あえて不確定な未来を生きていたのだ。</div>
                        <div class="p-3 bg-black/40 rounded" data-lang-key="db.history.4">🌅 没案庫の余白<br>中下はその出会いを公式記録から抹消し、調律師だけの「没案庫」にそっと書き残した。<br><br>没案記録 No.！？-β「杖を持たないという選択」<br>安定は正義ではない。だが不安定もまた、悪ではない。 世界は“確定された問い”だけでは、前に進めない。<br><br>魔王の熱を内包した「‽」の調律、そして杖を持たぬ者たちの意志。 全てを包み込んだ和温陣国の空で、鮮やかな国旗は、今日も新しく、静かに揺れている。</div>
                    </div>
                </section>

                <!-- Q&A and Glossary -->
                <section class="grid md:grid-cols-2 gap-6">
                    <div class="card p-6 bg-zinc-900/90 border border-white/10 space-y-4">
                        <h3 class="text-lg font-bold pixel-font text-red-500 mb-2" data-lang-key="db.qa.title">Q&A・公文書質問箱</h3>
                        <div class="text-xs space-y-3 text-zinc-300">
                            <div><p class="font-bold text-yellow-400" data-lang-key="db.qa.q1">Q. T.Sと絡んだらどうなるのか？</p><p data-lang-key="db.qa.a1">A. そもそも関われません。T.Sは和温陣国において「最重要人物」といっても過言ではない人物です。</p></div>
                            <div><p class="font-bold text-yellow-400" data-lang-key="db.qa.q2">Q. 無理やり関わったら？</p><p data-lang-key="db.qa.a2">A. 死にます。また、生き残ったとしても、極刑及び死刑。「複数の異常団体の実験道具になります。」「人型で帰れたら奇跡レベル」</p></div>
                            <div><p class="font-bold text-yellow-400" data-lang-key="db.qa.q3">Q. T.Sと関わる方法はありますか？</p><p data-lang-key="db.qa.a3">A. あります。<br>・和温陣国の政府に許可証を提出し、インタビューを行う<br>・T.S本人に事前に許可をとる(証明する方法も込み)<br>・異常存在に巻き込まれた時(首都内)に異常対策本部に救助され保護される</p></div>
                            <div><p class="font-bold text-yellow-400" data-lang-key="db.qa.q4">Q. 同一アート作家Rとの関係は？</p><p data-lang-key="db.qa.a4">A. よく分かってません。関わったのにも関わらず生きて帰ったのは確かです。</p></div>
                            <div><p class="font-bold text-yellow-400" data-lang-key="db.qa.q5">Q. 首都以外に行く方法はありますか？</p><p data-lang-key="db.qa.a5">A. 許可証を発行してもらえれば、自由に散策することができます。しかし、観光目的で首都以外に行く行為は推奨されません。行くんだったら安全対策をしっかりして、目的を持っていきましょう。</p></div>
                            <div><p class="font-bold text-yellow-400" data-lang-key="db.qa.q6">Q. 首都以外に行ったらどうなりますか？</p><p data-lang-key="db.qa.a6">A. 空間の歪みに巻き込まれる影響は未知数です。運が良ければ壁に埋まるぐらいで済みますが、悪ければ自分が壁になったり、液体になったりします。安全対策はしっかりしてから移動しましょう。</p></div>
                            <div><p class="font-bold text-yellow-400" data-lang-key="db.qa.q7">Q. onvaの人と関わってもいいの？</p><p data-lang-key="db.qa.a7">A. 別に話しても良いですが、onvaのことを聞くのは禁止となっています。<br>理由: onvaが最適化された監視国家だから。</p></div>
                        </div>
                    </div>

                    <div class="card p-6 bg-zinc-900/90 border border-white/10 space-y-4">
                        <h3 class="text-lg font-bold pixel-font text-purple-400 mb-2" data-lang-key="db.glossary.title">用語：ザラヴァサ（zaravasa）</h3>
                        <div class="text-xs text-zinc-300 leading-relaxed bg-black/40 p-4 rounded border border-white/5" data-lang-key="db.glossary.desc">
                            ※1 onvaに住んでる人でザラヴァサ（zaravasa）した人が稀に移住している<br><br><b>ザラヴァサ（zaravasa） [形]</b><br>シェルアップ語が元。最適化されすぎて精神的・肉体的に疲弊した状態。主にonvaから来た移住者が使う表現。
                        </div>
                    </div>
                </section>
            </div>
        </div>

    </main>

    <!-- フッター -->
    <footer id="contact" class="bg-black py-16 border-t border-white/10">
        <div class="max-w-6xl mx-auto px-6 text-center">
            <div class="text-2xl font-bold pixel-font mb-6 tracking-widest text-zinc-400" data-lang-key="footer.title">和温陣国</div>
            <div class="flex justify-center gap-8 mb-8">
                <a href="https://ec2045.github.io/WZN/" target="_blank" class="text-yellow-600 hover:text-yellow-400 transition text-sm font-bold pixel-font" data-lang-key="footer.wzn">WZN-和温放送局</a>
            </div>
            <p class="text-zinc-700 text-[10px]" data-lang-key="footer.copy">&copy; 2024 Wajin-Tofu Records. All Rights Reserved.</p>
        </div>
    </footer>

    <!-- 入国審査モーダル -->
    <div id="entryModal" class="modal fixed inset-0 z-[100] hidden bg-black/95 backdrop-blur-md overflow-y-auto">
        <div class="bg-zinc-900 max-w-lg mx-auto my-10 p-8 border border-white/10 relative shadow-2xl">
            <span class="absolute top-4 right-4 text-3xl cursor-pointer text-zinc-500 hover:text-white" onclick="closeModal('entryModal')">&times;</span>
            <div class="mb-6 border-b border-blue-600/30 pb-4">
                <h2 class="text-2xl font-bold pixel-font text-blue-500 italic" data-lang-key="modal.entry.title">大陸入国審査フォーム</h2>
            </div>
            <form id="entryForm" onsubmit="handleEntrySubmission(event)">
                <div class="space-y-4">
                    <div>
                        <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.entry.name">申請者名</label>
                        <input type="text" id="entryName" required placeholder="Name / ID">
                    </div>
                    <div>
                        <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.entry.purpose">入国目的</label>
                        <textarea id="entryPurpose" rows="3" required placeholder="目的を記入してください"></textarea>
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.entry.type">所持杖の種類</label>
                            <select id="staffType">
                                <option value="standard" data-lang-key="modal.entry.type.op1">一般用（標準）</option>
                                <option value="unstable" data-lang-key="modal.entry.type.op2">不安定（魔王領産）</option>
                                <option value="none" data-lang-key="modal.entry.type.op3">未所持</option>
                            </select>
                        </div>
                        <div>
                            <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.entry.travel">渡航方法</label>
                            <select id="travelMode">
                                <option value="sea" data-lang-key="modal.entry.travel.op1">海上（定期船）</option>
                                <option value="teleport" data-lang-key="modal.entry.travel.op2">陣（空間転移）</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex items-start gap-3 p-4 bg-white/5 border border-white/10 mt-6">
                        <input type="checkbox" required class="w-5 h-5 mt-1 cursor-pointer">
                        <span class="text-[10px] text-zinc-400" data-lang-key="modal.entry.check">私は和温陣国の法を遵守し、「安定」を乱さないことを誓います。</span>
                    </div>
                </div>
                <button type="submit" id="submitBtn" class="w-full bg-blue-600 text-white py-4 mt-8 font-bold hover:bg-blue-700 transition pixel-font" data-lang-key="modal.entry.submit">申請データを送信</button>
            </form>
        </div>
    </div>

    <!-- 国勢調査モーダル -->
    <div id="censusModal" class="modal fixed inset-0 z-[100] hidden bg-black/95 backdrop-blur-md overflow-y-auto">
        <div class="bg-zinc-900 max-w-lg mx-auto my-10 p-8 border border-white/10 relative shadow-2xl">
            <span class="absolute top-4 right-4 text-3xl cursor-pointer text-zinc-500 hover:text-white" onclick="closeModal('censusModal')">&times;</span>
            <div class="mb-6 border-b border-red-600/30 pb-4">
                <h2 class="text-2xl font-bold pixel-font text-red-500 italic" data-lang-key="modal.census.title">第1回 和温陣国 国勢調査</h2>
                <p class="text-[10px] text-zinc-500 mt-1 uppercase" data-lang-key="modal.census.sub">National Population Census</p>
            </div>
            <form onsubmit="handleCensusSubmission(event)">
                <div class="space-y-5">
                    <div>
                        <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.census.loc">現在の居住地</label>
                        <select required>
                            <option value="" data-lang-key="modal.census.loc.op0">選択してください</option>
                            <option value="capital" data-lang-key="modal.census.loc.op1">和陣当府（中央）</option>
                            <option value="boundary" data-lang-key="modal.census.loc.op2">ラ＝ウクカ境界（緩衝区）</option>
                            <option value="unstable" data-lang-key="modal.census.loc.op3">不安定の地（旧領）</option>
                            <option value="external" data-lang-key="modal.census.loc.op4">国外 / 渡航中</option>
                        </select>
                    </div>
                    <div>
                        <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.census.age">年齢層</label>
                        <select required>
                            <option value="under20" data-lang-key="modal.census.age.op1">20歳未満</option>
                            <option value="20-40" data-lang-key="modal.census.age.op2">20代〜40代</option>
                            <option value="40-60" data-lang-key="modal.census.age.op3">40代〜60代</option>
                            <option value="over60" data-lang-key="modal.census.age.op4">60歳以上</option>
                            <option value="immortal" data-lang-key="modal.census.age.op5">不老長寿</option>
                        </select>
                    </div>
                    <div>
                        <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.census.stab">現在の「安定」度合（自己申告）</label>
                        <input type="range" min="1" max="100" value="80" class="w-full h-2 bg-zinc-800 rounded-lg appearance-none cursor-pointer accent-red-600">
                        <div class="flex justify-between text-[10px] text-zinc-600 mt-1">
                            <span data-lang-key="modal.census.stab.l">不安定</span>
                            <span data-lang-key="modal.census.stab.m">中立</span>
                            <span data-lang-key="modal.census.stab.r">完全安定</span>
                        </div>
                    </div>
                    <div>
                        <label class="text-xs text-zinc-500 block mb-1" data-lang-key="modal.census.req">政府への要望・意見</label>
                        <textarea placeholder="（例）杖の配給を増やしてほしい、等" rows="3"></textarea>
                    </div>
                </div>
                <button type="submit" class="w-full bg-zinc-100 text-black py-4 mt-8 font-bold hover:bg-red-600 hover:text-white transition pixel-font" data-lang-key="modal.census.submit">回答を正式送信</button>
            </form>
        </div>
    </div>

    <!-- メッセージボックス -->
    <div id="msgBox" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-[200] hidden">
        <div class="bg-zinc-900 border-2 border-white p-8 text-center shadow-[0_0_50px_rgba(0,0,0,1)]">
            <div id="msgIcon" class="text-4xl mb-4">📋</div>
            <p id="msgText" class="text-xl pixel-font mb-6 leading-relaxed"></p>
            <button onclick="hideMsg()" class="bg-white text-black px-10 py-2 font-bold pixel-font hover:bg-zinc-200 transition" data-lang-key="msg.btn">確認</button>
        </div>
    </div>
  <script src="src/script_0c08256f.js"></script>
</body>
</html>
"""

with open("/Users/rituto/Documents/GitHub/Waon-Jinkoku/index.html", "w") as f:
    f.write(html_content)
