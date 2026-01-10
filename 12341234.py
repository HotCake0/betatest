import json
import requests
import os

# 팀 리스트 정의
red_team = {
    "dmng50" : "빵땅콩"
}

blue_team = {
    "bach023" : "울산큰고래",
    "gyeonjahee" : "견자희",
    "kimmaren77" : "김마렌",
    "gatgdf" : "쏭이",
    "xpdpfv2" : "이지수",
    "doki0818" : "감자가비"
}

green_team = {
    "e9dongsung" : "추멘",
    "eunchr" : "은초롱",
    "phs6162" : "찐랑",
    "imhanbily" : "한비",
    "cosmicaaarrr" : "아르르",
    "angel000429" : "베지"
}

yellow_team = {
    "land4968" : "야무지",
    "top6373" : "란다",
    "koo2202" : "구본좌",
    "not15987" : "다뮤",
    "sellkey" : "셀키"
}

purple_team = {
    "jaeparkk" : "박재박",
    "hhr001234" : "어쩜냥이",
    "leesoi34" : "냥쏘",
    "yeyo25" : "예요예요",
    "morgan427" : "숙희",
    "nslah830" : "피치"
}

def check_member_live(bj_id, bj_name):
    url = f"https://bjapi.afreecatv.com/api/{bj_id}/station"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        broad_data = data.get("broad")
        if broad_data:
            broad_no = broad_data.get("broad_no")
            return {
                "id": bj_id,
                "name": bj_name,
                "is_live": True,
                "title": broad_data.get('broad_title', ''),
                "viewers": broad_data.get('current_sum_viewer', 0),
                "thumbnail": f"https://liveimg.afreecatv.com/m/{broad_no}",
                "live_url": f"https://play.sooplive.co.kr/{bj_id}/{broad_no}"
            }
        return {"id": bj_id, "name": bj_name, "is_live": False}
    except:
        return {"id": bj_id, "name": bj_name, "is_live": False}

def save_team_status(team_dict, filename):
    results = []
    for bj_id, bj_name in team_dict.items():
        info = check_member_live(bj_id, bj_name)
        results.append(info)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print(f"✅ {filename} 업데이트 완료!")

if __name__ == '__main__':
    save_team_status(red_team, 'red_team_status.json')
    save_team_status(blue_team, 'blue_team_status.json')
    save_team_status(green_team, 'green_team_status.json')
    save_team_status(yellow_team, 'yellow_team_status.json')
    save_team_status(purple_team, 'purple_team_status.json')
