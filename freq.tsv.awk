{ words[$0]++ }
END {
	for (w in words)
		printf("%d\t%s\n", words[w], w)
}
