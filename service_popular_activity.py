from time import sleep
import json

def listen_request():
    with open('request_most_popular.txt', 'r+') as f:
        txt_command = f.read()
        
        if txt_command == 'WHAT_IS_THE_MOST_POPULAR_ACTIVITY':            
            activity = find_popular_activity()
            
            # Clear the file content and move to the beinning of the file             
            f.truncate(0)
            f.seek(0)            
            f.write(activity)
            
            
def find_popular_activity():
    with open('content_rated.js') as f:
        pop_act = ''
        pop_score = 0
        
        data = json.load(f)
        print (data)
        
        # Find the activity having the highest score
        for act_object in data:
            if act_object['score'] >= pop_score:
                pop_score = act_object['score']
                pop_act = act_object['activity']
        
        print(pop_act) 
        return pop_act   
    
if __name__ == "__main__":
    while True:
        #sleep(1)
        listen_request()