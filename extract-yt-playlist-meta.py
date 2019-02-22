with open('playlist-meta.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

count = 0
video_title = ""
video_link = ""
video_description = ""

for idx, line in enumerate(content):
    if 'ERROR' in line:
        count = 0
    else:
        if count == 2 or count == 3 or count == 4:
            if count == 2:
                video_link_idx = line.index(' u') + 3
                video_link = "https://www.youtube.com/watch?v=" + line[video_link_idx:video_link_idx+11]
            elif count == 3:
                video_title_idx = line.index(' u') + 3
                video_title_end_idx = line.rfind(")") - 1
                video_title = line[video_title_idx:video_title_end_idx]
            elif count == 4:
                video_description_idx = line.index(' u') + 3
                video_description_end_idx = line.rfind(")") - 1
                video_description = line[video_description_idx:video_description_end_idx]
            count += 1
        else:
            if count == 5:
                count = 0
                print("@" + video_title + "@" + video_link + "@" + video_description)
            else:
                count += 1
