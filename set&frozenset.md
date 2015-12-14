<a target="_blank" href="https://docs.python.org/2.7/library/stdtypes.html#set-types-set-frozenset">官方文档</a>

<table>
    <tr>
        <td>方法名</td>
        <td>作用</td>
    </tr>
    <tr>
        <td>创建set</td>
        <td>sa = set([1,2,3])或者sb = set((1,2,3))</td>
    </tr>
    <tr>
        <td>创建frozenset</td>
        <td>sa = frozenset([1,2,3])或者sb = frozenset((1,2,3))</td>
    </tr>
    <tr>
        <td>len(s)</td>
        <td>返回s的长度</td>
    </tr>
    <tr>
        <td>x in s</td>
        <td>x在s里返回True,否则返回False</td>
    </tr>
    <tr>
        <td>x not in s</td>
        <td>x不在s里返回True,否则返回False</td>
    </tr>
    <tr>
        <td>isdisjoint(other)</td>
        <td>
        sa.isdisjoint(sb)<br>
        是否交集,若sb&sa==set([]),返回True.
        </td>
    </tr>
    <tr>
        <td>issubset(other)</td>
        <td>sa.issubset(sb)<br>
            sa是否包含sb,相当于sa>=sb   
        </td>
    </tr>
    <tr>
        <td>set <= other</td>
        <td>sa<=sb</td>
    </tr>
    <tr>
        <td>issuperset(other)</td>
        <td>相当于sa<=sb</td>
    </tr>
    <tr>
        <td>union(other, ...)</td>
        <td>sc=sa.union(sb), 返回sa和sb的所有元素<br>相当于set | other | ...</td>
    </tr>
    <tr>
        <td>intersection(other, ...)</td>
        <td>sc=sa.intersection(sb),返回sa和sb都有的元素<br>相当于set & other & ...</td>
    </tr>
    <tr>
        <td>difference(other, ...)</td>
        <td>差集,相当于set - other - ...</td>
    </tr>
    <tr>
        <td>symmetric_difference(other)</td>
        <td>sc= sa ^ sb 相当于 (sa-sb)|(sb-sa)</td>
    </tr>
    <tr>
        <td>copy()</td>
        <td>浅拷贝，a=[1, ['a', 'b']],b = copy.copy(a) <br>
          修改a[0]的元素,b不会修改，但是修改a[1]的元素,b会跟着修改</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
    </tr>
</table>
    <tr>
        <td></td>
        <td></td>
    </tr>
