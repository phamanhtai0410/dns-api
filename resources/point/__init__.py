from resources.point.total_points import PointServiceResource
from resources.point.claim_point import ClaimPointServiceResource
from resources.point.default_points import DefaultPointsResource
from resources.point.mint_logs import MintLogsResource
point_resourses = {
    # "/history": PointServiceResource,
    "/total_point": PointServiceResource,
    "/claim_point": ClaimPointServiceResource,
    "/default_point":DefaultPointsResource,
    "/mint_logs": MintLogsResource
}