import json

class HashtagManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_hashtags(self, name):
        hashtag_list = ''
        i = 0
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            for hashtag in data['hashtags']:
                if hashtag['name'] == name:
                    for hastags in hashtag['hashtag_list']:
                        #if it's the last hashtag, don't add a comma
                        if i == len(hashtag['hashtag_list'])-1:
                            hashtag_list += hastags
                        else:
                            hashtag_list += hastags + ','
                        i += 1
                    return hashtag_list
            
    def get_hashtags_title(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            return [hashtag['name'] for hashtag in data['hashtags']]
        
    def update_hashtags(self, name, hashtag_list):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            for hashtag in data['hashtags']:
                if hashtag['name'] == name:
                    hashtag['hashtag_list'] = hashtag_list.split(',')
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_hashtags_to_preset(self, name, hashtag_list):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            for hashtag in data['hashtags']:
                if hashtag['name'] == name:
                    for hastags in hashtag_list.split(','):
                        hashtag['hashtag_list'].append(hastags)
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)


    def add_preset_hashtags(self, name, hashtag_list):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            data['hashtags'].append({'name':name, 'hashtag_list':hashtag_list.split()})
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def delete_hashtags(self, name):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            for hashtag in data['hashtags']:
                if hashtag['name'] == name:
                    data['hashtags'].remove(hashtag)
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)


