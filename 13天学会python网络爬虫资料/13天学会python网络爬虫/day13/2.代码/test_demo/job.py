import schedule


def job():
    print(123)


def main():
    schedule.every(3).seconds.do(job)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()
