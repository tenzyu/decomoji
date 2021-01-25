from os import getenv

from dotenv import load_dotenv

load_dotenv()

# get token from .env
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")

# setting
BOT_NAME = "Decomoji"
BOT_PREFIX = "!"
WEBHOOK_NAME = "Decomoji"
EMOJI_IDS = {
    "あ": "792941871466807319",
    "い": "792941871218950174",
    "う": "792941871667085372",
    "え": "792941871621996575",
    "お": "792941871747563580",
    "か": "792941871780986895",
    "き": "792941871193128994",
    "く": "792941871327739904",
    "け": "792941871532867584",
    "こ": "792941871155773441",
    "さ": "792941871600631808",
    "し": "792941871189590056",
    "す": "792941871839707137",
    "せ": "792941871638380555",
    "そ": "792941870807384125",
    "た": "792941871541518366",
    "ち": "792941871282257961",
    "つ": "792941871210692648",
    "て": "792941870766227458",
    "と": "792941871633924126",
    "な": "792941871676260372",
    "に": "792941869297565726",
    "ぬ": "792941869150633984",
    "ね": "792941869063340063",
    "の": "792941869297565706",
    "は": "792941869171605554",
    "ひ": "792941869642022962",
    "ふ": "792941869179863060",
    "へ": "792941869332037643",
    "ほ": "792941868722683936",
    "ま": "792941869008289814",
    "み": "792941868685590549",
    "む": "792941869013270568",
    "め": "792941868743786527",
    "も": "792941868807487489",
    "や": "792941868970410034",
    "ゆ": "792941869004619806",
    "よ": "792941868945506334",
    "ら": "792941868861751296",
    "り": "792941869180518410",
    "る": "792941868995706961",
    "れ": "792941869012090882",
    "ろ": "792941868907233320",
    "わ": "792941868920602664",
    "を": "792941868953632798",
    "ん": "792941868807618560",
    "が": "793107423686033450",
    "ぎ": "793107423174721536",
    "ぐ": "793107422663016479",
    "げ": "793107423987499018",
    "ご": "793107422788452382",
    "ざ": "793107423547097131",
    "じ": "793107422851235850",
    "ず": "793107423757992036",
    "ぜ": "793107423761661962",
    "ぞ": "793107423061082152",
    "だ": "793107423555485737",
    "ぢ": "793107422872076348",
    "づ": "793107422944296980",
    "で": "793107422679531561",
    "ど": "793107424160383016",
    "ば": "793107424893599784",
    "び": "793107424214646824",
    "ぶ": "793107424185024532",
    "べ": "793107424348471296",
    "ぼ": "793107424201408512",
    "ぱ": "793107424185679872",
    "ぴ": "793107423468584970",
    "ぷ": "793107423509610537",
    "ぺ": "793107421530423337",
    "ぽ": "793107421769891840",
    "ぁ": "793107419252129807",
    "ぃ": "793107419777335296",
    "ぅ": "793107419521220638",
    "ぇ": "793107419475214346",
    "ぉ": "793107419437465622",
    "っ": "793107419411775520",
    "ゃ": "793107418980155483",
    "ゅ": "793107419159855165",
    "ょ": "793107419064041485",
    "〜": "793685199321956412",
    "ー": "793685199321956412",
    "1": "793681374406115340",
    "2": "793681374727897158",
    "3": "793681374891737088",
    "4": "793681375366348830",
    "5": "793681374615699476",
    "6": "793681375197790218",
    "7": "793681374645059594",
    "8": "793681374774296576",
    "9": "793681374191419392",
    "0": "793681375273287711",
    "１": "793681374406115340",
    "２": "793681374727897158",
    "３": "793681374891737088",
    "４": "793681375366348830",
    "５": "793681374615699476",
    "６": "793681375197790218",
    "７": "793681374645059594",
    "８": "793681374774296576",
    "９": "793681374191419392",
    "０": "793681375273287711",
    "-": "793683224038473728",
    "/": "793683227566145586",
    "／": "793683227566145586",
    ":": "793683228442624071",
    "：": "793683228442624071",
    "@": "793683229189865493",
    "＠": "793683229189865493",
    "(": "793683228476571660",
    "（": "793683228476571660",
    ")": "793683228741468160",
    "）": "793683228741468160",
    "｢": "793683226584809472",
    "「": "793683226584809472",
    "｣": "793683225830359040",
    "」": "793683225830359040",
    "¥": "793683228254273547",
    "￥": "793683228254273547",
    "&": "793683227155496961",
    "＆": "793683227155496961",
    "。": "793683216337993738",
    "、": "793683216220422224",
    "!": "793683216237723708",
    "！": "793683216237723708",
    "?": "793683216015163453",
    "？": "793683216015163453",
    "[": "793684836883628053",
    "［": "793684836883628053",
    "]": "793684837629558794",
    "］": "793684837629558794",
    "{": "793684837311315988",
    "｛": "793684837311315988",
    "}": "793684836933304371",
    "｝": "793684836933304371",
    "#": "793684837936267295",
    "＃": "793684837936267295",
    "%": "793684838334332948",
    "％": "793684838334332948",
    "^": "793684836506140692",
    "＾": "793684836506140692",
    "*": "793684838397640745",
    "＊": "793684838397640745",
    "+": "793684837033574421",
    "＋": "793684837033574421",
    "=": "793684836975116338",
    "＝": "793684836975116338",
    "_": "793687852248465430",
    "\\": "793687852139282432",
    "＼": "793687852139282432",
    ";": "793687852088426517",
    "；": "793687852088426517",
    "|": "793687852117917707",
    "｜": "793687852117917707",
    "<": "793687853027950622",
    "＜": "793687853027950622",
    ">": "793687853188120597",
    "＞": "793687853188120597",
    "“": "793687853003571211",
    "”": "793687852839731220",
    "‘": "793687851795349533",
    "’": "793687852114116618",
    "$": "793687853556957184",
    "＄": "793687853556957184",
    "€": "793687852541411359",
    "・": "793687850871816192",
    "~": "793687850762633216",
}