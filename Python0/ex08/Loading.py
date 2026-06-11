import os


def ft_tqdm(lst: range) -> None:
	"""

	"""
	totlen = len(lst)
	start = os.times()[4]

	terminal = os.get_terminal_size().columns
	bar_size = terminal - 41

	for i, item in enumerate(lst):
		step = i + 1
		progress = int(step / totlen * bar_size)
		curr_time = os.times()[4]
		elapsed_time = curr_time - start
		speed = step / elapsed_time if elapsed_time > 0 else 0
		eta = (totlen - step) / speed if elapsed_time > 0 else 0

		format_time = f"{int(elapsed_time // 60):02d}:{int(elapsed_time % 60):02d}"
		format_eta = f"{int(eta // 60):02d}:{int(eta % 60):02d}"

		bar = f"|{'█' * progress:<{bar_size}}|"
		percent = progress * 100 // bar_size

		print(f"{percent}%{bar} {step}/{totlen} [{format_time}<{format_eta} {speed:.2f}it/s]", end="\r", flush=True)
		yield item


def main():
	for _ in ft_tqdm(0, 333):
		pass


if __name__ == "__main__":
	main()
