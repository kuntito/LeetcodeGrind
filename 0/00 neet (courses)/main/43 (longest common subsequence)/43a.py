# https://leetcode.com/problems/longest-common-subsequence/description/

def print_commons(text1, text2):
    text1_set = set(text1)
    text2_set = set(text2)

    text1 = ''.join(ch for ch in text1 if ch in text2_set)
    text2 = ''.join(ch for ch in text2 if ch in text1_set)

    print(f'["{text1}", "{text2}"],')    


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        grid = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]


        for ri in range(rows-1, -1, -1):
            for ci in range(cols-1, -1, -1):
                if text1[ri] == text2[ci]:
                    grid[ri][ci] = grid[ri+1][ci+1] + 1
                else:
                    grid[ri][ci] = max(grid[ri+1][ci], grid[ri][ci+1])

        # for row in grid:
        #     print(row)

        return grid[0][0]


    # def explore_pos(self, start_pos, matches):
    #     if matches[start_pos]:
    #         return matches[start_pos]
        
    #     length = 0
    #     for pos in matches:
    #         if pos[0] <= start_pos[0] or\
    #             pos[1] <= start_pos[1]:
    #                 continue
    #         length = max(
    #             length,
    #             self.explore_pos(pos, matches)
    #         )
            
    #     matches[start_pos] = length + 1
    #     return matches[start_pos]


# items = [
#     ["abcde", "ace"],
#     ["abc", "abc"],
#     ["abc", "def"],
#     ["bl", "yby"],
#     ["ezupkr", "ubmrapg"],
#     ["oxcpqrsvwf", "shmtulqrypy"],
#     ["abcba", "abcbcba"],
#     ["bsbininm", "jmjkbkjkv"],
#     ["bbm", "mb"],
#     ["aaa", "aaa"],
# ]

items = [
    ["", ""],
    ["upr", "urp"],
    ["ace", "ace"],
    ["pqrs", "sqrp"],
    ["ab", "abc"],
    ["bbm", "mb"],
    ["hcbgcrcbh", "ghbrgc"],
    ["abcde", "ace"],
    ["bsbininm", "jmjkbkjkv"],
    ["abcba", "abcbcba"],
    # ["fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny", "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"],
    # ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # ],
    # ["aaa", "aaa"],

]

sol = Solution()
# for text1, text2 in items:
#     res = sol.longestCommonSubsequence(text1, text2)


uno, dos = items[-1]
# uno, dos = ["mhuuzqzsiwbu", "szusmhwziwbq"]
# uno, dos = ["pmjghexybyrgzczy", "hafcdqbgncrcbihkd"]
# uno, dos = ["hcbgcrcbh", "ghbrgc"]
print_commons(uno, dos)
res = sol.longestCommonSubsequence(uno, dos)
print(res)