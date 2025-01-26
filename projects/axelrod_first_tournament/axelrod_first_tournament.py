import axelrod as axl
import matplotlib.pyplot as plt

first_tournament_participants_ordered_by_reported_rank = [s() for s in axl.axelrod_first_strategies]

number_of_strategies = len(first_tournament_participants_ordered_by_reported_rank)

for player in first_tournament_participants_ordered_by_reported_rank:
    print(player)

tournament = axl.Tournament(
    players=first_tournament_participants_ordered_by_reported_rank,
    turns=200,
    repetitions=5,
    seed=1,
)

results = tournament.play()

for name in results.ranked_names:
    print(name)


plt.figure(figsize=(15, 6))

plt.plot((0, 15), (0, 15), color="grey", linestyle="--")

for original_rank, strategy in enumerate(
    first_tournament_participants_ordered_by_reported_rank
):

    rank = results.ranked_names.index(str(strategy))

    if rank == original_rank:

        symbol = "+"

        plt.plot((rank, rank), (rank, 0), color="grey")

    else:

        symbol = "o"

    plt.scatter([rank], [original_rank], marker=symbol, color="black", s=50)

plt.xticks(range(number_of_strategies), results.ranked_names, rotation=90)

plt.ylabel("Reported rank")

plt.xlabel("Reproduced rank")

plt.show()


plot = axl.Plot(results)

p = plot.boxplot()

p.show()
