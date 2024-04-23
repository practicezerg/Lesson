# -*- encoding: utf-8 -*-


from config import *

# write step scripts

def write_step(step_log):
	#перезаписывает каждый шаг для новой попытки
	with open(steps_log ,"a",encoding="utf-8") as a:
		a.write(str(step_log)+"\n")
		
# write start/stop scripts

def final_log(start_time, end_time):
	end = end_time.time()
	start = start_time.time()
	msg = f"{get_str_date_now()}		{script_name} start {start} end {end} time work = {end_time-start_time}! \n"
	with open(f"{path_for_log}log_work_scripts.txt", "a", encoding="utf=8") as a: 
		a.write(msg)


def counts_results(data):
	with open(f"{path_for_log}all_count_try.txt", "r+", encoding="utf-8") as r:
		lines = r.readlines()
		"""
		lines[2] - Количество всего попыток
		lines[4] - Количество успешных попыток
		lines[6] - Попытки завершились ошибкой
		lines[8] - Процент успехных попыток
		"""
		if data == "start":
			mistake = int(lines[2])-int(lines[4])
			proc = (int(lines[4])/int(lines[2]))*100
			num = int(lines[2]) + 1
			lines[2] = str(num) + "\n"
			lines[6] = str(mistake) + "\n"
			lines[8] = str(proc) + "%\n"
			r.seek(0)
			r.writelines(lines)
		else:
			num = int(lines[4]) + 1
			lines[4] = str(num) + "\n"
			r.seek(0)
			r.writelines(lines)

