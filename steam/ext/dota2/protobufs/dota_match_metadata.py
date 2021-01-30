# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_match_metadata.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto

from .base_gcmessages import CsoEconItem
from .dota_gcmessages_common import CMsgDotaMatch, CMsgMatchTips
from .dota_gcmessages_common_match_management import CLobbyTimedRewardDetails, CMsgMatchMatchmakingStats, CMvpData
from .dota_shared_enums import EdotammrBoostType, EEvent


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataFile(betterproto.Message):
    version: int = betterproto.int32_field(1)
    match_id: int = betterproto.uint64_field(2)
    metadata: "CdotaMatchMetadata" = betterproto.message_field(3)
    private_metadata: bytes = betterproto.bytes_field(5)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadata(betterproto.Message):
    teams: List["CdotaMatchMetadataTeam"] = betterproto.message_field(1)
    item_rewards: List["CLobbyTimedRewardDetails"] = betterproto.message_field(2)
    lobby_id: int = betterproto.fixed64_field(3)
    report_until_time: int = betterproto.fixed64_field(4)
    event_game_custom_table: bytes = betterproto.bytes_field(5)
    primary_event_id: int = betterproto.uint32_field(6)
    match_tips: List["CMsgMatchTips"] = betterproto.message_field(7)
    matchmaking_stats: "CMsgMatchMatchmakingStats" = betterproto.message_field(8)
    mvp_data: "CMvpData" = betterproto.message_field(9)
    guild_challenge_progress: List["CdotaMatchMetadataGuildChallengeProgress"] = betterproto.message_field(10)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeam(betterproto.Message):
    dota_team: int = betterproto.uint32_field(1)
    players: List["CdotaMatchMetadataTeamPlayer"] = betterproto.message_field(2)
    graph_experience: List[float] = betterproto.float_field(3)
    graph_gold_earned: List[float] = betterproto.float_field(4)
    graph_net_worth: List[float] = betterproto.float_field(5)
    cm_first_pick: bool = betterproto.bool_field(6)
    cm_captain_player_id: int = betterproto.uint32_field(7)
    cm_bans: List[int] = betterproto.uint32_field(8)
    cm_picks: List[int] = betterproto.uint32_field(9)
    cm_penalty: int = betterproto.uint32_field(10)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamPlayerKill(betterproto.Message):
    victim_slot: int = betterproto.uint32_field(1)
    count: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamItemPurchase(betterproto.Message):
    item_id: int = betterproto.uint32_field(1)
    purchase_time: int = betterproto.int32_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamInventorySnapshot(betterproto.Message):
    item_id: List[int] = betterproto.uint32_field(1)
    game_time: int = betterproto.int32_field(2)
    kills: int = betterproto.uint32_field(3)
    deaths: int = betterproto.uint32_field(4)
    assists: int = betterproto.uint32_field(5)
    level: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamAutoStyleCriteria(betterproto.Message):
    name_token: int = betterproto.uint32_field(1)
    value: float = betterproto.float_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamStrangeGemProgress(betterproto.Message):
    kill_eater_type: int = betterproto.uint32_field(1)
    gem_item_def_index: int = betterproto.uint32_field(2)
    required_hero_id: int = betterproto.uint32_field(3)
    starting_value: int = betterproto.uint32_field(4)
    ending_value: int = betterproto.uint32_field(5)
    owner_item_def_index: int = betterproto.uint32_field(6)
    owner_item_id: int = betterproto.uint64_field(7)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamVictoryPrediction(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    item_def_index: int = betterproto.uint32_field(2)
    starting_value: int = betterproto.uint32_field(3)
    is_victory: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamSubChallenge(betterproto.Message):
    slot_id: int = betterproto.uint32_field(1)
    start_value: int = betterproto.uint32_field(2)
    end_value: int = betterproto.uint32_field(3)
    completed: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamCavernChallengeResult(betterproto.Message):
    completed_path_id: int = betterproto.uint32_field(1)
    claimed_room_id: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamActionGrant(betterproto.Message):
    action_id: int = betterproto.uint32_field(1)
    quantity: int = betterproto.uint32_field(2)
    audit: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamCandyGrant(betterproto.Message):
    points: int = betterproto.uint32_field(1)
    reason: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamEventData(betterproto.Message):
    event_id: int = betterproto.uint32_field(1)
    event_points: int = betterproto.uint32_field(2)
    challenge_instance_id: int = betterproto.uint32_field(3)
    challenge_quest_id: int = betterproto.uint32_field(4)
    challenge_quest_challenge_id: int = betterproto.uint32_field(5)
    challenge_completed: bool = betterproto.bool_field(6)
    challenge_rank_completed: int = betterproto.uint32_field(7)
    challenge_rank_previously_completed: int = betterproto.uint32_field(8)
    event_owned: bool = betterproto.bool_field(9)
    sub_challenges_with_progress: List["CdotaMatchMetadataTeamSubChallenge"] = betterproto.message_field(10)
    wager_winnings: int = betterproto.uint32_field(11)
    cavern_challenge_active: bool = betterproto.bool_field(12)
    cavern_challenge_winnings: int = betterproto.uint32_field(13)
    amount_wagered: int = betterproto.uint32_field(14)
    periodic_point_adjustments: int = betterproto.uint32_field(16)
    cavern_challenge_map_results: List["CdotaMatchMetadataTeamCavernChallengeResult"] = betterproto.message_field(17)
    cavern_challenge_plus_shard_winnings: int = betterproto.uint32_field(18)
    actions_granted: List["CdotaMatchMetadataTeamActionGrant"] = betterproto.message_field(19)
    cavern_crawl_map_variant: int = betterproto.uint32_field(20)
    team_wager_bonus_pct: int = betterproto.uint32_field(21)
    wager_streak_pct: int = betterproto.uint32_field(22)
    candy_points_granted: List["CdotaMatchMetadataTeamCandyGrant"] = betterproto.message_field(23)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamGauntletProgress(betterproto.Message):
    gauntlet_tier: int = betterproto.uint32_field(2)
    gauntlet_wins: int = betterproto.uint32_field(3)
    gauntlet_losses: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamPlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    ability_upgrades: List[int] = betterproto.uint32_field(2)
    player_slot: int = betterproto.uint32_field(3)
    equipped_econ_items: List["CsoEconItem"] = betterproto.message_field(4)
    kills: List["CdotaMatchMetadataTeamPlayerKill"] = betterproto.message_field(5)
    items: List["CdotaMatchMetadataTeamItemPurchase"] = betterproto.message_field(6)
    avg_kills_x16: int = betterproto.uint32_field(7)
    avg_deaths_x16: int = betterproto.uint32_field(8)
    avg_assists_x16: int = betterproto.uint32_field(9)
    avg_gpm_x16: int = betterproto.uint32_field(10)
    avg_xpm_x16: int = betterproto.uint32_field(11)
    best_kills_x16: int = betterproto.uint32_field(12)
    best_assists_x16: int = betterproto.uint32_field(13)
    best_gpm_x16: int = betterproto.uint32_field(14)
    best_xpm_x16: int = betterproto.uint32_field(15)
    win_streak: int = betterproto.uint32_field(16)
    best_win_streak: int = betterproto.uint32_field(17)
    fight_score: float = betterproto.float_field(18)
    farm_score: float = betterproto.float_field(19)
    support_score: float = betterproto.float_field(20)
    push_score: float = betterproto.float_field(21)
    level_up_times: List[int] = betterproto.uint32_field(22)
    graph_net_worth: List[float] = betterproto.float_field(23)
    inventory_snapshot: List["CdotaMatchMetadataTeamInventorySnapshot"] = betterproto.message_field(24)
    avg_stats_calibrated: bool = betterproto.bool_field(25)
    auto_style_criteria: List["CdotaMatchMetadataTeamAutoStyleCriteria"] = betterproto.message_field(26)
    event_data: List["CdotaMatchMetadataTeamEventData"] = betterproto.message_field(29)
    strange_gem_progress: List["CdotaMatchMetadataTeamStrangeGemProgress"] = betterproto.message_field(30)
    hero_xp: int = betterproto.uint32_field(31)
    camps_stacked: int = betterproto.uint32_field(32)
    victory_prediction: List["CdotaMatchMetadataTeamVictoryPrediction"] = betterproto.message_field(33)
    lane_selection_flags: int = betterproto.uint32_field(34)
    rampages: int = betterproto.uint32_field(35)
    triple_kills: int = betterproto.uint32_field(36)
    aegis_snatched: int = betterproto.uint32_field(37)
    rapiers_purchased: int = betterproto.uint32_field(38)
    couriers_killed: int = betterproto.uint32_field(39)
    net_worth_rank: int = betterproto.uint32_field(40)
    support_gold_spent: int = betterproto.uint32_field(41)
    observer_wards_placed: int = betterproto.uint32_field(42)
    sentry_wards_placed: int = betterproto.uint32_field(43)
    wards_dewarded: int = betterproto.uint32_field(44)
    stun_duration: float = betterproto.float_field(45)
    rank_mmr_boost_type: "EdotammrBoostType" = betterproto.enum_field(46)
    gauntlet_progress: "CdotaMatchMetadataTeamGauntletProgress" = betterproto.message_field(47)
    contract_progress: List["CdotaMatchMetadataTeamPlayerContractProgress"] = betterproto.message_field(48)
    guild_ids: List[int] = betterproto.uint32_field(49)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataTeamPlayerContractProgress(betterproto.Message):
    guild_id: int = betterproto.uint32_field(1)
    event_id: int = betterproto.uint32_field(2)
    challenge_instance_id: int = betterproto.uint32_field(3)
    challenge_parameter: int = betterproto.uint32_field(4)
    contract_stars: int = betterproto.uint32_field(5)
    contract_slot: int = betterproto.uint32_field(6)
    completed: bool = betterproto.bool_field(7)


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataGuildChallengeProgress(betterproto.Message):
    guild_id: int = betterproto.uint32_field(1)
    event_id: "EEvent" = betterproto.enum_field(2)
    challenge_instance_id: int = betterproto.uint32_field(3)
    challenge_parameter: int = betterproto.uint32_field(4)
    challenge_timestamp: int = betterproto.uint32_field(5)
    challenge_progress_at_start: int = betterproto.uint32_field(6)
    challenge_progress_accumulated: int = betterproto.uint32_field(7)
    individual_progress: List["CdotaMatchMetadataGuildChallengeProgressIndividualProgress"] = betterproto.message_field(
        8
    )


@dataclass(eq=False, repr=False)
class CdotaMatchMetadataGuildChallengeProgressIndividualProgress(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    progress: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadata(betterproto.Message):
    teams: List["CdotaMatchPrivateMetadataTeam"] = betterproto.message_field(1)
    graph_win_probability: List[float] = betterproto.float_field(2)
    string_names: List["CdotaMatchPrivateMetadataStringName"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataStringName(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeam(betterproto.Message):
    dota_team: int = betterproto.uint32_field(1)
    players: List["CdotaMatchPrivateMetadataTeamPlayer"] = betterproto.message_field(2)
    buildings: List["CdotaMatchPrivateMetadataTeamBuilding"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    player_slot: int = betterproto.uint32_field(2)
    position_stream: bytes = betterproto.bytes_field(3)
    combat_segments: List["CdotaMatchPrivateMetadataTeamPlayerCombatSegment"] = betterproto.message_field(4)
    damage_unit_names: List[str] = betterproto.string_field(5)
    buff_records: List["CdotaMatchPrivateMetadataTeamPlayerBuffRecord"] = betterproto.message_field(6)
    graph_kills: List[float] = betterproto.float_field(7)
    graph_deaths: List[float] = betterproto.float_field(8)
    graph_assists: List[float] = betterproto.float_field(9)
    graph_lasthits: List[float] = betterproto.float_field(10)
    graph_denies: List[float] = betterproto.float_field(11)
    gold_received: "CdotaMatchPrivateMetadataTeamPlayerGoldReceived" = betterproto.message_field(12)
    xp_received: "CdotaMatchPrivateMetadataTeamPlayerXpReceived" = betterproto.message_field(13)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerCombatSegment(betterproto.Message):
    game_time: int = betterproto.int32_field(1)
    damage_by_ability: List[
        "CdotaMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbility"
    ] = betterproto.message_field(2)
    healing_by_ability: List[
        "CdotaMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbility"
    ] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbility(betterproto.Message):
    source_unit_index: int = betterproto.uint32_field(3)
    ability_id: int = betterproto.uint32_field(1)
    by_hero_targets: List[
        "CdotaMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbilityByHeroTarget"
    ] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerCombatSegmentDamageByAbilityByHeroTarget(betterproto.Message):
    hero_id: int = betterproto.uint32_field(1)
    damage: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbility(betterproto.Message):
    source_unit_index: int = betterproto.uint32_field(3)
    ability_id: int = betterproto.uint32_field(1)
    by_hero_targets: List[
        "CdotaMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbilityByHeroTarget"
    ] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerCombatSegmentHealingByAbilityByHeroTarget(betterproto.Message):
    hero_id: int = betterproto.uint32_field(1)
    healing: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerBuffRecord(betterproto.Message):
    buff_ability_id: int = betterproto.uint32_field(1)
    buff_modifier_name: str = betterproto.string_field(3)
    by_hero_targets: List["CdotaMatchPrivateMetadataTeamPlayerBuffRecordByHeroTarget"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerBuffRecordByHeroTarget(betterproto.Message):
    hero_id: int = betterproto.uint32_field(1)
    elapsed_duration: float = betterproto.float_field(2)
    is_hidden: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerGoldReceived(betterproto.Message):
    creep: int = betterproto.uint32_field(1)
    heroes: int = betterproto.uint32_field(2)
    bounty_runes: int = betterproto.uint32_field(3)
    passive: int = betterproto.uint32_field(4)
    buildings: int = betterproto.uint32_field(5)
    abilities: int = betterproto.uint32_field(6)
    wards: int = betterproto.uint32_field(7)
    other: int = betterproto.uint32_field(8)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamPlayerXpReceived(betterproto.Message):
    creep: int = betterproto.uint32_field(1)
    heroes: int = betterproto.uint32_field(2)
    roshan: int = betterproto.uint32_field(3)
    tome_of_knowledge: int = betterproto.uint32_field(4)
    outpost: int = betterproto.uint32_field(5)
    other: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class CdotaMatchPrivateMetadataTeamBuilding(betterproto.Message):
    unit_name: str = betterproto.string_field(1)
    position_quant_x: int = betterproto.uint32_field(2)
    position_quant_y: int = betterproto.uint32_field(3)
    death_time: float = betterproto.float_field(4)


@dataclass(eq=False, repr=False)
class CMsgDotadpcMatch(betterproto.Message):
    match: "CMsgDotaMatch" = betterproto.message_field(1)
    metadata: "CdotaMatchMetadata" = betterproto.message_field(2)
