def hanoi(n, source, destination, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, aux, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, aux, destination, source)


hanoi(4, source='A', destination='C', aux='B')