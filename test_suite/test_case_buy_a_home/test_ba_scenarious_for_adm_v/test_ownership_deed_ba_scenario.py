import random

import logging

import pytest

from utils.api_library import Status
from utils.json_parser import JsonParser


class TestAdmBuahBA(object):
    """Test cases related to test_ADM BA scenario v.0.3"""

    @pytest.mark.parametrize("plot_id", [
        476702, 476803, 476823, 476363, 476447, 476535, 476623, 476771, 476824, 476402, 476490,
        476578, 476666, 476734, 476798, 476364, 476448, 476536, 476825, 476491, 476579, 476667,
        476799, 476385, 476777, 476715, 476670, 476781])
    def test_ownership_deed(self, plot_id, api_helper):
        """Test GetUnitOwnershipDeed: BUAH-2259"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetUnitOwnershipDeed",
                                                                                "TAMMPropertyProfileService",
                                                                                "getUnitOwnershipDeedBAv03",
                                                                                args=plot_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        OwnerId = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                             'GetUnitOwnershipDeedResult',
                                                             'UnitOwnershipDeed', 'OwnershipDeedShareDetailsList',
                                                             'OwnershipDeedShareDetails',
                                                             'OwnerId'])
        PlotOwnerShareId = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                      'GetUnitOwnershipDeedResult',
                                                                      'UnitOwnershipDeed',
                                                                      'OwnershipDeedShareDetailsList',
                                                                      'OwnershipDeedShareDetails',
                                                                      'PlotOwnerShareId'])

        UnitClassificationNameA = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                             'GetUnitOwnershipDeedResult',
                                                                             'UnitOwnershipDeed',
                                                                             'UnitClassificationNameA'])

        OwnerName = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                               'GetUnitOwnershipDeedResult',
                                                               'UnitOwnershipDeed',
                                                               'OwnershipDeedShareDetailsList',
                                                               'OwnershipDeedShareDetails',
                                                               'OwnerName'])

        OwnershipPercentage = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                         'GetUnitOwnershipDeedResult',
                                                                         'UnitOwnershipDeed',
                                                                         'OwnershipDeedShareDetailsList',
                                                                         'OwnershipDeedShareDetails',
                                                                         'OwnershipPercentage'])
        print(
            "Plot_IDs_for_Ansam = %s, OwnerId = %s, PlotOwnerShareId = %s,  UnitClassificationNameA = %s, "
            "OwnerName = %s, OwnershipPercentage = %s"
            % (plot_id, OwnerId, PlotOwnerShareId, UnitClassificationNameA, OwnerName, OwnershipPercentage))

    @pytest.mark.parametrize("plot_id", [
        446942, 447214, 446840, 447482, 447016, 447257])
    def test_ownership_deed_2(self, plot_id, api_helper):
        """Test GetUnitOwnershipDeed: BUAH-2259"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetUnitOwnershipDeed",
                                                                                "TAMMPropertyProfileService",
                                                                                "getUnitOwnershipDeedBAv03",
                                                                                args=plot_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        OwnerId = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                             'GetUnitOwnershipDeedResult',
                                                             'UnitOwnershipDeed', 'OwnershipDeedShareDetailsList',
                                                             'OwnershipDeedShareDetails',
                                                             'OwnerId'])
        PlotOwnerShareId = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                      'GetUnitOwnershipDeedResult',
                                                                      'UnitOwnershipDeed',
                                                                      'OwnershipDeedShareDetailsList',
                                                                      'OwnershipDeedShareDetails',
                                                                      'PlotOwnerShareId'])

        UnitClassificationNameA = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                             'GetUnitOwnershipDeedResult',
                                                                             'UnitOwnershipDeed',
                                                                             'UnitClassificationNameA'])


        OwnerName = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                               'GetUnitOwnershipDeedResult',
                                                               'UnitOwnershipDeed',
                                                               'OwnershipDeedShareDetailsList',
                                                               'OwnershipDeedShareDetails',
                                                               'OwnerName'])

        OwnershipPercentage = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                         'GetUnitOwnershipDeedResult',
                                                                         'UnitOwnershipDeed',
                                                                         'OwnershipDeedShareDetailsList',
                                                                         'OwnershipDeedShareDetails',
                                                                         'OwnershipPercentage'])
        print(
            "Plot_IDs_for_Ansam = %s, OwnerId = %s, PlotOwnerShareId = %s,  UnitClassificationNameA = %s, "
            "OwnerName = %s, OwnershipPercentage = %s"
            % (plot_id, OwnerId, PlotOwnerShareId, UnitClassificationNameA, OwnerName, OwnershipPercentage))