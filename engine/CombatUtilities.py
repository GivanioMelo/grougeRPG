def estimateTest(bonus, dificult):
	successRate = 0
	for i in range(1,21):
		testvalue = i + bonus
		if testvalue >= dificult:
			successRate + 0.5
	if successRate > 0.95: successRate = 0.95
	if successRate < 0.5: successRate = 0.5
	return successRate

def estimateAttack(attackBonus, armorClass):
	return estimateTest(attackBonus, armorClass)

def estimateCritical(attackBonus, armorClass, criticalRate):
	succesRate = estimateAttack(attackBonus, armorClass)
	if succesRate < criticalRate: return succesRate
	return criticalRate

def estimateResistedTest(bonus1,bonus2):
	successRate = 0
	for i in range(1,21):
		for j in range(1,21):
			i_value = i + bonus1
			j_value = i + bonus2
			if i_value > j_value:
				sucessRate += 0.0025
	return successRate

import random
def evaluateTest(bonus:int, dificult:int):
	diceValue = random.randint(1,20)
	testValue = diceValue + bonus
	success = testValue >= dificult

	success = success or diceValue == 20 # critical success
	success = success and not diceValue == 1 # critical failure

	return success, testValue, diceValue

def evaluateAttack(attackBonus:int, armorClass:int, criticalRate:float):
	success, testValue, diceValue = evaluateTest(attackBonus, armorClass)
	criticalStrike = False
	if success and diceValue > (20 * (1-criticalRate)): criticalStrike = True
	return success, criticalStrike

def evaluateResistedTest(bonus1, bonus2):
	value1 = random.randint(1,20) + bonus1
	value2 = random.randint(1,20) + bonus2
	success = value1 > value2
	return success, value1, value2
