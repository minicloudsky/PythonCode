class Tactics:
    """
    算路偏好，该参数只对驾车算路 (driving) 生效。 该服务为满足性能需求，不含道路阻断信息干预。
可选值：
10： 不走高速；
11：常规路线，即多数用户常走的一条经验路线，满足大多数场景需求，是较推荐的一个策略
12： 距离较短（考虑路况）：即距离相对较短的一条路线，但并不一定是一条优质路线。
计算耗时时，考虑路况对耗时的影响；
13： 距离较短（不考虑路况）：路线同以上，但计算耗时时，不考虑路况对耗时的影响，
可理解为在路况完全通畅时预计耗时。
注：除 13 外，其他偏好的耗时计算都考虑实时路况
    """
    NOT_HIGHWAY = 10
    ROUTINE = 11
    SHORT_DISTANCE_CONSIDER = 12
    SHORT_DISTANCE_NOT_CONSIDER = 13


class ServiceAddress:
    # 驾车
    driving = 'driving'
    # 骑行
    riding = 'riding'
    # 步行
    walking = 'walking'


class Time:
    minute = '分钟'
    hour = '小时'
    day = '天'
