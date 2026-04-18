neetcode took a different approach.

he mapped every character to it's suffixes.

the cross-iterated every character with every other character.
on each iteration, he'd find the unique suffixes in both groups.

multiply their counts.
and voila, you'd have the unique ways you can combine both words.

sum up all the unique ways and you have your result.

# TODO write your own breakdown with these insights in mind.