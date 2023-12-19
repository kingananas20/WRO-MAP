def getCode(distanceList, angleList):
    print(f"{distanceList}\n{angleList}")
    for distance, angle in zip(distanceList, angleList):
        if -5 < angle < 5:
            print(f"Strecke({distance})")
        elif 85 < angle < 95:
            print(f"Drehung(1, 0, 0, 90)\nStrecke(0, 0, {distance})")
        elif -95 < angle -85:
            print(f"Drehung(1, 0, 0, -90)\nStrecke(0, 0, {distance})")
        elif 175 < angle < -175:
            print(f"Strecke(0, 0, -10)")
            if distance < 10:
                return
            print(f"Drehung(1, 0, 0, 180)\nStrecke(0, 0, {distance - 10})")
        else:
            print(f"Drehung(1, 0, 0, {angle})\nStrecke(0, 0, {distance})")

if __name__ == "__main__":
    print("Loaded Code")