print("Chapter 6:")
print("Exercise 14 - Nesting Dictionaries in a List")

# You can nest dictionaries in a list
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print("---")
# Often, you'll do this sort of nesting iteratively as needed
aliens = []

# Add 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Change the speed on the first three aliens
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# Display the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total aliens: {len(aliens)}")
