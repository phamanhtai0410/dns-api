from resources.point.total_points import PointServiceResource
from resources.point.claim_point import ClaimPointServiceResource
from resources.point.default_points import DefaultPointsResource
point_resourses = {
    # "/history": PointServiceResource,
    "/total_point": PointServiceResource,
    "/claim_point": ClaimPointServiceResource,
    "/default_point":DefaultPointsResource
}