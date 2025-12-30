class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict

        # Create a mapping from pairs of blocks to possible top blocks
        allowed_map = defaultdict(set)
        for triplet in allowed:
            allowed_map[triplet[:2]].add(triplet[2])

        def can_build_pyramid(current_level: str) -> bool:
            if len(current_level) == 1:
                return True

            # Generate all possible next levels
            next_level_options = []

            for i in range(len(current_level) - 1):
                pair = current_level[i:i + 2]
                if pair not in allowed_map:
                    return False
                next_level_options.append(allowed_map[pair])

            # Backtrack through all combinations of the next level
            def backtrack(index: int, next_level: str) -> bool:
                if index == len(next_level_options):
                    return can_build_pyramid(next_level)

                for block in next_level_options[index]:
                    if backtrack(index + 1, next_level + block):
                        return True
                return False

            return backtrack(0, "")

        return can_build_pyramid(bottom)
    
