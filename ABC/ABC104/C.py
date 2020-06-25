d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]


def dfs(i, sum, count, nokori):
    global ans
    if i == d:#全ての最後の問題セットにたどり着いたら,　全ての葉を確認
        if sum < g:
            use = max(nokori)#選んでいない種類で最大のスコアの問題を選ぶ
            #-(-(g-sum)//(use*100)) <- (g-sum)//(use*100)　199//100 = 0, -199//100 = -1 なので最低超えている数が欲しいときはマイナスに変換する。
            n = min(pc[use-1][0], -(-(g-sum)//(use*100)))#その難易度の問題の数 または 残りの必要スコア/その難易度の問題1問の点数　の最小値をとる->余計に問題を解かない＆問題数を超えてとかない
            print(n, -(-(g-sum)//(use*100)), (g-sum), -(g-sum)//(use*100))
            count += n
            sum += n * use * 100

        if sum >= g:#全ての葉の達成してる最小の答えを記録
            ans = min(ans, count)

    else:
        dfs(i+1, sum, count, nokori)#選ばなかった場合
        dfs(i+1, sum + pc[i][0] * (i+1) * 100 + pc[i][1], count + pc[i][0], nokori - {i+1})#全て解いた番号をセットから抜いて、合計&countを更新

ans = float("inf")
dfs(0, 0, 0, set(range(1, d+1)))
print(ans)