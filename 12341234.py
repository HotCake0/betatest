import json
import requests
import os

# 팀 리스트 정의
red_team = {
    "apaceh2401": "디엘",
    "opix" : "태양권",
    "qw0949" : "조혜원",
    "indian6402" : "후",
    "chloesy" : "우서",
    "whiteone325" : "난워니",
    "minguri1016" : "배민정"
}

blue_team = {
    "bach023" : "울산큰고래",
    "kimmaren77" : "김마렌",
    "gatgdf" : "쏭이",
    "xpdpfv2" : "이지수"
}

# [추가] 진행팀(매니저) 리스트
manager_team = {
    "pubgbjmatch": "멸망전"
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
    # [추가] 진행팀 파일 생성
    save_team_status(manager_team, 'manager_status.json')
