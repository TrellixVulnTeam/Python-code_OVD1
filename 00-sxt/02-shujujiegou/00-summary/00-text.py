'''
总结一下

Python 数据结构和算法。

最近下班一直在学习和总结Python，最近在整理数据结构和算法这方面的知识，虽然大学的时候也学过数据结构(c语言版本)，
但是工作这几年一直在做前端所以，这方面的知识也忘了差不多，所以就想整理一下，方便以后自己复习。

作为程序员肯定对数据结构和算法这两个概念不陌生,我先不说这两个概念具体的定义是什么，后续会慢慢说明。

一、引入
    我们先看一道题
    “如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?”

    查看 01-demo.py
    我们可以看到 运行的时间:214.583347秒

    算法的概念是：算法是计算机处理信息的本质，因为计算机程序本质上是一个算法来告诉计算机确切的步骤来执行一个任务。简单来说就是
    算法是告诉计算机第一步干什么。第二步干什么....，然后就任务完成OK，

    算法是独立存在的一种解决问题的方法和思想。
    比如说上面这个问题，在JavaScript语言里面实现的语法就不一样了，但是解决这个问题的思路是一样的。

    对于算法而言，实现的语言并不重要，重要的是思想。

    算法的五大特性：（了解）
    1、输入：算法具有0个或者多个输入。
    2、输出：算法至少有1个或者多个输出。（算法就是结果问题，解决问题后总要有个结果吧）
    3、又穷性：算法在有限的步骤之后会自动结束而不会无限循环。
    4、确定性：算法中的每一步都有确定的含义，不会出现二义性，
    5、可行性：算法的每一步都是可行的。

    那还还是对于上面的问题我们是不是还有其他方法呢，我们可以看到 上面 a + b + c = 1000 所以如果知道了 a b 那么自然就知道了C

    查看 02-demo.py

    我们可以看到 运行的时间:0.182897秒

    大家看到这个执行时间会有什么想法呢，我的想法是第二个算法的效率真高！
    这两个算法不同，那么算法的效率怎么衡量呢？
    我们最直观的感觉是执行时间，比如上面两个算法，200多秒和1秒的差距还是挺大的。所以我们可以直观的得出一个结论
    ”实现算法程序的执行时间可以反映出算法的效率，即算法的优劣“

    但是我们单看从执行时间来判断算法的优劣，这样可信吗！

    假设我们将第二次尝试的算法程序运行在一台配置古老性能低下的计算机中，情况会如何？
    很可能运行的时间并不会比在我们的电脑中运行算法一的214.583347秒快多少。

    单纯依靠运行的时间来比较算法的优劣并不一定是客观准确的！

    程序的运行离不开计算机环境（包括硬件和操作系统），这些客观原因会影响程序运行的速度并反应在程序的执行时间上。
    为了客观的反映出算法的优劣，提出了时间复杂度与“大O记法”

    时间复杂度与“大O记法”

    我们假定计算机执行算法每一个基本操作的时间是固定的一个时间单位，那么有多少个基本操作就会花费多少时间单位。
    虽然对于不同的机器环境而言，确切的单位时间是不同的，但是对于算法进行多少个基本操作（即花费的时间单位）在规模
    数量级却是相同的，由此可以忽略机器环境的影响而客观的反应算法的时间效率。

    简单来说 就是基本操作的数量。

    我们先看01-demo.py这个算法的操作的基本数量,对于一些加减乘除赋值来说，每一都算一个 步骤
    1000 * 1000 * 1000 * 9
    如果有 n 个话
    n * n *n *9 = n^3 * 9

    我们看 02-demo.py 这个算法的步骤
    1000 * 1000 * 9
    如果有n 个的话
    n *n * 9 = n^2 * 9

    我们可以看到基本操作的数量表示

    我们先看一下 大O表示法的概念。
    “大O记法：对于单调的整数函数f,如果存在一个整数函数g和实常数c>0,使得对于充分大的n总有f(n) < c*g(n)，就是说函数g是f的一个渐进函数（忽略常数），
    记为f(n) = O(g(n))。也就是说，在趋向无穷的极限意义下，函数f的增长速度受到函数g的约束，亦即函数f与函数g的特征相似”

    时间复杂度：假设存在函数g，使得算法A处理规模为n的问题示例所用时间为T(n)=O(g(n))，则称O(g(n))为算法A的渐近时间复杂度，
    简称时间复杂度，记为T(n)


    如何理解“大O记法”
    对于算法进行特别具体的细致分析虽然很好，但在实践中的实际价值有限。
    对于算法的时间性质和空间性质，最重要的是其数量级和趋势，这些是分析算法效率的主要部分。
    而计量算法基本操作数量的规模函数中那些常量因子可以忽略不计。
    例如，可以认为3n^2和100n^2属于同一个量级，如果两个算法处理同样规模实例的代价分别为这两个函数，就认为它们的效率“差不多”，都为n^2级。

    最坏时间复杂度
    我们主要关注算法的最坏情况，亦即最坏时间复杂度

    算法分析
    01-demo.py 的T(n) = O(n*n*n) = O(N^3)
    02-demo.py 的T(n) = O(n*n) = O(N^2)

    由此可见，第二种算法要比第一种算法的时间复杂度好多了。


    常见时间复杂度


    常见时间复杂度之间的关系
    O(1) < O(log*n) < O(n) < O(n*log*n) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)

二、Python内置类型性能分析

三、数据结构

    概念
        数据是一个抽象的概念，将其进行分类后得到程序设计语言中的基本类型。如 int string float ...
        数据元素之间不是独立的，存在特定的关系，这些关系便是结构。数据结构指数据对象中数据元素之间的关系。


'''