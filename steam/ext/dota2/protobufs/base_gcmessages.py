# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: base_gcmessages.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


class EGCBaseProtoObjectTypes(betterproto.Enum):
    PartyInvite = 1001
    LobbyInvite = 1002


class ECustomGameInstallStatus(betterproto.Enum):
    Unknown = 0
    Ready = 1
    Busy = 2
    FailedGeneric = 101
    FailedInternalError = 102
    RequestedTimestampTooOld = 103
    RequestedTimestampTooNew = 104
    CRCMismatch = 105
    FailedSteam = 106
    FailedCanceled = 107


class CMsgExtractGemsResponseEExtractGems(betterproto.Enum):
    Succeeded = 0
    ToolIsInvalid = 1
    ItemIsInvalid = 2
    ToolCannotRemoveGem = 3
    FailedToRemoveGem = 4


class CMsgAddSocketResponseEAddSocket(betterproto.Enum):
    Succeeded = 0
    ToolIsInvalid = 1
    ItemCannotBeSocketed = 2
    FailedToAddSocket = 3


class CMsgAddItemToSocketResponseEAddGem(betterproto.Enum):
    Succeeded = 0
    GemIsInvalid = 1
    ItemIsInvalid = 2
    FailedToAddGem = 3
    InvalidGemTypeForSocket = 4
    InvalidGemTypeForHero = 5
    InvalidGemTypeForSlot = 6
    SocketContainsUnremovableGem = 7


class CMsgResetStrangeGemCountResponseEResetGem(betterproto.Enum):
    Succeeded = 0
    FailedToResetGem = 1
    ItemIsInvalid = 2
    InvalidSocketId = 3
    SocketCannotBeReset = 4


@dataclass
class CGCStorePurchaseInitLineItem(betterproto.Message):
    item_def_id: int = betterproto.uint32_field(1)
    quantity: int = betterproto.uint32_field(2)
    cost_in_local_currency: int = betterproto.uint32_field(3)
    purchase_type: int = betterproto.uint32_field(4)
    source_reference_id: int = betterproto.uint64_field(5)


@dataclass
class CMsgGCStorePurchaseInit(betterproto.Message):
    country: str = betterproto.string_field(1)
    language: int = betterproto.int32_field(2)
    currency: int = betterproto.int32_field(3)
    line_items: List["CGCStorePurchaseInitLineItem"] = betterproto.message_field(4)


@dataclass
class CMsgGCStorePurchaseInitResponse(betterproto.Message):
    result: int = betterproto.int32_field(1)
    txn_id: int = betterproto.uint64_field(2)


@dataclass
class CMsgSystemBroadcast(betterproto.Message):
    message: str = betterproto.string_field(1)


@dataclass
class CMsgClientPingData(betterproto.Message):
    relay_codes: List[float] = betterproto.fixed32_field(4)
    relay_pings: List[int] = betterproto.uint32_field(5)
    region_codes: List[int] = betterproto.uint32_field(8)
    region_pings: List[int] = betterproto.uint32_field(9)
    region_ping_failed_bitmask: int = betterproto.uint32_field(10)


@dataclass
class CMsgInviteToParty(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    client_version: int = betterproto.uint32_field(2)
    team_id: int = betterproto.uint32_field(3)
    as_coach: bool = betterproto.bool_field(4)
    ping_data: "CMsgClientPingData" = betterproto.message_field(5)


@dataclass
class CMsgInviteToLobby(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    client_version: int = betterproto.uint32_field(2)


@dataclass
class CMsgInvitationCreated(betterproto.Message):
    group_id: int = betterproto.uint64_field(1)
    steam_id: float = betterproto.fixed64_field(2)
    user_offline: bool = betterproto.bool_field(3)


@dataclass
class CMsgPartyInviteResponse(betterproto.Message):
    party_id: int = betterproto.uint64_field(1)
    accept: bool = betterproto.bool_field(2)
    client_version: int = betterproto.uint32_field(3)
    ping_data: "CMsgClientPingData" = betterproto.message_field(8)


@dataclass
class CMsgLobbyInviteResponse(betterproto.Message):
    lobby_id: float = betterproto.fixed64_field(1)
    accept: bool = betterproto.bool_field(2)
    client_version: int = betterproto.uint32_field(3)
    custom_game_crc: float = betterproto.fixed64_field(6)
    custom_game_timestamp: float = betterproto.fixed32_field(7)


@dataclass
class CMsgKickFromParty(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)


@dataclass
class CMsgLeaveParty(betterproto.Message):
    pass


@dataclass
class CMsgCustomGameInstallStatus(betterproto.Message):
    status: "ECustomGameInstallStatus" = betterproto.enum_field(1)
    message: str = betterproto.string_field(2)
    latest_timestamp_from_steam: float = betterproto.fixed32_field(3)


@dataclass
class CMsgServerAvailable(betterproto.Message):
    custom_game_install_status: "CMsgCustomGameInstallStatus" = (
        betterproto.message_field(1)
    )


@dataclass
class CMsgLANServerAvailable(betterproto.Message):
    lobby_id: float = betterproto.fixed64_field(1)


@dataclass
class CSOEconGameAccountClient(betterproto.Message):
    additional_backpack_slots: int = betterproto.uint32_field(1)
    trial_account: bool = betterproto.bool_field(2)
    eligible_for_online_play: bool = betterproto.bool_field(3)
    need_to_choose_most_helpful_friend: bool = betterproto.bool_field(4)
    in_coaches_list: bool = betterproto.bool_field(5)
    trade_ban_expiration: float = betterproto.fixed32_field(6)
    duel_ban_expiration: float = betterproto.fixed32_field(7)
    made_first_purchase: bool = betterproto.bool_field(9)


@dataclass
class CSOItemCriteriaCondition(betterproto.Message):
    op: int = betterproto.int32_field(1)
    field: str = betterproto.string_field(2)
    required: bool = betterproto.bool_field(3)
    float_value: float = betterproto.float_field(4)
    string_value: str = betterproto.string_field(5)


@dataclass
class CSOItemCriteria(betterproto.Message):
    item_level: int = betterproto.uint32_field(1)
    item_quality: int = betterproto.int32_field(2)
    item_level_set: bool = betterproto.bool_field(3)
    item_quality_set: bool = betterproto.bool_field(4)
    initial_inventory: int = betterproto.uint32_field(5)
    initial_quantity: int = betterproto.uint32_field(6)
    ignore_enabled_flag: bool = betterproto.bool_field(8)
    conditions: List["CSOItemCriteriaCondition"] = betterproto.message_field(9)
    recent_only: bool = betterproto.bool_field(10)


@dataclass
class CSOItemRecipe(betterproto.Message):
    def_index: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    n_a: str = betterproto.string_field(3)
    desc_inputs: str = betterproto.string_field(4)
    desc_outputs: str = betterproto.string_field(5)
    di_a: str = betterproto.string_field(6)
    di_b: str = betterproto.string_field(7)
    di_c: str = betterproto.string_field(8)
    do_a: str = betterproto.string_field(9)
    do_b: str = betterproto.string_field(10)
    do_c: str = betterproto.string_field(11)
    requires_all_same_class: bool = betterproto.bool_field(12)
    requires_all_same_slot: bool = betterproto.bool_field(13)
    class_usage_for_output: int = betterproto.int32_field(14)
    slot_usage_for_output: int = betterproto.int32_field(15)
    set_for_output: int = betterproto.int32_field(16)
    input_items_criteria: List["CSOItemCriteria"] = betterproto.message_field(20)
    output_items_criteria: List["CSOItemCriteria"] = betterproto.message_field(21)
    input_item_dupe_counts: List[int] = betterproto.uint32_field(22)


@dataclass
class CMsgApplyStrangePart(betterproto.Message):
    strange_part_item_id: int = betterproto.uint64_field(1)
    item_item_id: int = betterproto.uint64_field(2)


@dataclass
class CMsgApplyPennantUpgrade(betterproto.Message):
    upgrade_item_id: int = betterproto.uint64_field(1)
    pennant_item_id: int = betterproto.uint64_field(2)


@dataclass
class CMsgApplyEggEssence(betterproto.Message):
    essence_item_id: int = betterproto.uint64_field(1)
    egg_item_id: int = betterproto.uint64_field(2)


@dataclass
class CSOEconItemAttribute(betterproto.Message):
    def_index: int = betterproto.uint32_field(1)
    value: int = betterproto.uint32_field(2)
    value_bytes: bytes = betterproto.bytes_field(3)


@dataclass
class CSOEconItemEquipped(betterproto.Message):
    new_class: int = betterproto.uint32_field(1)
    new_slot: int = betterproto.uint32_field(2)


@dataclass
class CSOEconItem(betterproto.Message):
    id: int = betterproto.uint64_field(1)
    account_id: int = betterproto.uint32_field(2)
    inventory: int = betterproto.uint32_field(3)
    def_index: int = betterproto.uint32_field(4)
    quantity: int = betterproto.uint32_field(5)
    level: int = betterproto.uint32_field(6)
    quality: int = betterproto.uint32_field(7)
    flags: int = betterproto.uint32_field(8)
    origin: int = betterproto.uint32_field(9)
    attribute: List["CSOEconItemAttribute"] = betterproto.message_field(12)
    interior_item: "CSOEconItem" = betterproto.message_field(13)
    style: int = betterproto.uint32_field(15)
    original_id: int = betterproto.uint64_field(16)
    equipped_state: List["CSOEconItemEquipped"] = betterproto.message_field(18)


@dataclass
class CMsgSortItems(betterproto.Message):
    sort_type: int = betterproto.uint32_field(1)


@dataclass
class CSOEconClaimCode(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    code_type: int = betterproto.uint32_field(2)
    time_acquired: int = betterproto.uint32_field(3)
    code: str = betterproto.string_field(4)


@dataclass
class CMsgUpdateItemSchema(betterproto.Message):
    items_game: bytes = betterproto.bytes_field(1)
    item_schema_version: float = betterproto.fixed32_field(2)
    items_game_url: str = betterproto.string_field(3)


@dataclass
class CMsgGCError(betterproto.Message):
    error_text: str = betterproto.string_field(1)


@dataclass
class CMsgRequestInventoryRefresh(betterproto.Message):
    pass


@dataclass
class CMsgConVarValue(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CMsgReplicateConVars(betterproto.Message):
    convars: List["CMsgConVarValue"] = betterproto.message_field(1)


@dataclass
class CMsgItemAcknowledged(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    inventory: int = betterproto.uint32_field(2)
    def_index: int = betterproto.uint32_field(3)
    quality: int = betterproto.uint32_field(4)
    rarity: int = betterproto.uint32_field(5)
    origin: int = betterproto.uint32_field(6)


@dataclass
class CMsgSetItemPositions(betterproto.Message):
    item_positions: List[
        "CMsgSetItemPositionsItemPosition"
    ] = betterproto.message_field(1)


@dataclass
class CMsgSetItemPositionsItemPosition(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    position: int = betterproto.uint32_field(2)


@dataclass
class CMsgGCNameItemNotification(betterproto.Message):
    player_steamid: float = betterproto.fixed64_field(1)
    item_def_index: int = betterproto.uint32_field(2)
    item_name_custom: str = betterproto.string_field(3)


@dataclass
class CMsgGCClientDisplayNotification(betterproto.Message):
    notification_title_localization_key: str = betterproto.string_field(1)
    notification_body_localization_key: str = betterproto.string_field(2)
    body_substring_keys: List[str] = betterproto.string_field(3)
    body_substring_values: List[str] = betterproto.string_field(4)


@dataclass
class CMsgGCShowItemsPickedUp(betterproto.Message):
    player_steamid: float = betterproto.fixed64_field(1)


@dataclass
class CMsgGCIncrementKillCountResponse(betterproto.Message):
    killer_account_id: int = betterproto.uint32_field(1)
    num_kills: int = betterproto.uint32_field(2)
    item_def: int = betterproto.uint32_field(3)
    level_type: int = betterproto.uint32_field(4)


@dataclass
class CSOEconItemDropRateBonus(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    expiration_date: float = betterproto.fixed32_field(2)
    bonus: float = betterproto.float_field(3)
    bonus_count: int = betterproto.uint32_field(4)
    item_id: int = betterproto.uint64_field(5)
    def_index: int = betterproto.uint32_field(6)
    seconds_left: int = betterproto.uint32_field(7)
    booster_type: int = betterproto.uint32_field(8)


@dataclass
class CSOEconItemLeagueViewPass(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    league_id: int = betterproto.uint32_field(2)
    itemindex: int = betterproto.uint32_field(4)
    grant_reason: int = betterproto.uint32_field(5)


@dataclass
class CSOEconItemEventTicket(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    event_id: int = betterproto.uint32_field(2)
    item_id: int = betterproto.uint64_field(3)


@dataclass
class CSOEconItemTournamentPassport(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    league_id: int = betterproto.uint32_field(2)
    item_id: int = betterproto.uint64_field(3)
    original_purchaser_id: int = betterproto.uint32_field(4)
    passports_bought: int = betterproto.uint32_field(5)
    version: int = betterproto.uint32_field(6)
    def_index: int = betterproto.uint32_field(7)
    reward_flags: int = betterproto.uint32_field(8)


@dataclass
class CMsgGCStorePurchaseCancel(betterproto.Message):
    txn_id: int = betterproto.uint64_field(1)


@dataclass
class CMsgGCStorePurchaseCancelResponse(betterproto.Message):
    result: int = betterproto.uint32_field(1)


@dataclass
class CMsgGCStorePurchaseFinalize(betterproto.Message):
    txn_id: int = betterproto.uint64_field(1)


@dataclass
class CMsgGCStorePurchaseFinalizeResponse(betterproto.Message):
    result: int = betterproto.uint32_field(1)
    item_ids: List[int] = betterproto.uint64_field(2)


@dataclass
class CMsgGCToGCBannedWordListUpdated(betterproto.Message):
    group_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgGCToGCDirtySDOCache(betterproto.Message):
    sdo_type: int = betterproto.uint32_field(1)
    key_uint64: int = betterproto.uint64_field(2)


@dataclass
class CMsgGCToGCDirtyMultipleSDOCache(betterproto.Message):
    sdo_type: int = betterproto.uint32_field(1)
    key_uint64: List[int] = betterproto.uint64_field(2)


@dataclass
class CMsgGCToGCApplyLocalizationDiff(betterproto.Message):
    language: int = betterproto.uint32_field(1)
    packed_diff: str = betterproto.string_field(2)


@dataclass
class CMsgGCToGCApplyLocalizationDiffResponse(betterproto.Message):
    success: bool = betterproto.bool_field(1)


@dataclass
class CMsgGCCollectItem(betterproto.Message):
    collection_item_id: int = betterproto.uint64_field(1)
    subject_item_id: int = betterproto.uint64_field(2)


@dataclass
class CMsgSDONoMemcached(betterproto.Message):
    pass


@dataclass
class CMsgGCToGCUpdateSQLKeyValue(betterproto.Message):
    key_name: str = betterproto.string_field(1)


@dataclass
class CMsgGCServerVersionUpdated(betterproto.Message):
    server_version: int = betterproto.uint32_field(1)


@dataclass
class CMsgGCClientVersionUpdated(betterproto.Message):
    client_version: int = betterproto.uint32_field(1)


@dataclass
class CMsgGCToGCWebAPIAccountChanged(betterproto.Message):
    pass


@dataclass
class CMsgRecipeComponent(betterproto.Message):
    subject_item_id: int = betterproto.uint64_field(1)
    attribute_index: int = betterproto.uint64_field(2)


@dataclass
class CMsgFulfillDynamicRecipeComponent(betterproto.Message):
    tool_item_id: int = betterproto.uint64_field(1)
    consumption_components: List["CMsgRecipeComponent"] = betterproto.message_field(2)


@dataclass
class CMsgGCClientMarketDataRequest(betterproto.Message):
    user_currency: int = betterproto.uint32_field(1)


@dataclass
class CMsgGCClientMarketDataEntry(betterproto.Message):
    item_def_index: int = betterproto.uint32_field(1)
    item_quality: int = betterproto.uint32_field(2)
    item_sell_listings: int = betterproto.uint32_field(3)
    price_in_local_currency: int = betterproto.uint32_field(4)


@dataclass
class CMsgGCClientMarketData(betterproto.Message):
    entries: List["CMsgGCClientMarketDataEntry"] = betterproto.message_field(1)


@dataclass
class CMsgExtractGems(betterproto.Message):
    tool_item_id: int = betterproto.uint64_field(1)
    item_item_id: int = betterproto.uint64_field(2)
    item_socket_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgExtractGemsResponse(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    response: "CMsgExtractGemsResponseEExtractGems" = betterproto.enum_field(2)


@dataclass
class CMsgAddSocket(betterproto.Message):
    tool_item_id: int = betterproto.uint64_field(1)
    item_item_id: int = betterproto.uint64_field(2)
    unusual: bool = betterproto.bool_field(3)


@dataclass
class CMsgAddSocketResponse(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    updated_socket_index: List[int] = betterproto.uint32_field(2)
    response: "CMsgAddSocketResponseEAddSocket" = betterproto.enum_field(3)


@dataclass
class CMsgAddItemToSocketData(betterproto.Message):
    gem_item_id: int = betterproto.uint64_field(1)
    socket_index: int = betterproto.uint32_field(2)


@dataclass
class CMsgAddItemToSocket(betterproto.Message):
    item_item_id: int = betterproto.uint64_field(1)
    gems_to_socket: List["CMsgAddItemToSocketData"] = betterproto.message_field(2)


@dataclass
class CMsgAddItemToSocketResponse(betterproto.Message):
    item_item_id: int = betterproto.uint64_field(1)
    updated_socket_index: List[int] = betterproto.uint32_field(2)
    response: "CMsgAddItemToSocketResponseEAddGem" = betterproto.enum_field(3)


@dataclass
class CMsgResetStrangeGemCount(betterproto.Message):
    item_item_id: int = betterproto.uint64_field(1)
    socket_index: int = betterproto.uint32_field(2)


@dataclass
class CMsgResetStrangeGemCountResponse(betterproto.Message):
    response: "CMsgResetStrangeGemCountResponseEResetGem" = betterproto.enum_field(1)


@dataclass
class CMsgGCToClientPollFileRequest(betterproto.Message):
    file_name: str = betterproto.string_field(1)
    client_version: int = betterproto.uint32_field(2)
    poll_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgGCToClientPollFileResponse(betterproto.Message):
    poll_id: int = betterproto.uint32_field(1)
    file_size: int = betterproto.uint32_field(2)


@dataclass
class CMsgGCToGCPerformManualOp(betterproto.Message):
    op_id: int = betterproto.uint64_field(1)
    group_code: int = betterproto.uint32_field(2)


@dataclass
class CMsgGCToGCPerformManualOpCompleted(betterproto.Message):
    success: bool = betterproto.bool_field(1)
    source_gc: int = betterproto.uint32_field(2)


@dataclass
class CMsgGCToGCReloadServerRegionSettings(betterproto.Message):
    pass
