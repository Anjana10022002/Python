is_logged_in = True
is_subscribed = False
user_credits = 100
max_credits = 200
min_credits = 50
credits_valid = (user_credits >= min_credits and user_credits <= max_credits) and (user_credits != min_credits)
bonus_eligible = is_subscribed or not (user_credits <= min_credits)
user_credits += 50
user_credits -= 20
user_credits *= 2
user_credits %= 150
power_result = user_credits ** 2
full_access = is_logged_in and is_subscribed
