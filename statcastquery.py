#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pybaseball import (playerid_lookup, statcast, statcast_pitcher, statcast_pitcher_spin, statcast_batter, 
plot_stadium)

# Pitchers

playerid_lookup('kershaw', 'clayton')

ck = statcast_pitcher('2021-04-01', '2021-05-30', 477132)
ck2 = statcast_pitcher_spin.statcast_pitcher_spin('2021-05-31','2021-10-04', 477132)
kershaw = pd.concat([ck, ck2])
# print(kershaw.shape)

kershaw.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                        'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                        'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                        'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                        'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                        'post_fld_score'], inplace = True)
# Create is_strike column
kershaw['is_strike'] = [1 if x != 'B' else 0 for x in kershaw['type']]
# Create pitch_count column
kershaw['pitch_count'] = kershaw[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

# Switch from catcher's perspective to pitcher's perspective
# Catcher's POV: (plate_x, plate_z)
# Pitcher's POV: (plate_-x, plate_z)
kershaw['plate_-x'] = -kershaw['plate_x']
# Switch HB to perspective of pitcher
# Catcher's POV: (pfx_x, pfx_z)
# Pitcher's POV: (pfx_-x, pfx_z)
kershaw['pfx_-x'] = -kershaw['pfx_x']
# HB and VB in feet should be in inches (*12)
#kershaw['pfx_x'] = 12 * kershaw['pfx_x']
kershaw['pfx_-x'] = 12 * kershaw['pfx_-x']
kershaw['pfx_z'] = 12 * kershaw['pfx_z']

# Add spin_eff and true_spin
kershaw['spin_eff'] =  round(np.cos(np.radians(kershaw['theta'])), 2)
kershaw['true_spin'] = kershaw['release_spin_rate'] * kershaw['spin_eff']

# Add bauer_units column
kershaw['bauer_units'] = kershaw['release_spin_rate'] / kershaw['release_speed']

# Replace values
kershaw['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                               ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)

# Make all events that aren't hits, outs
kershaw['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                           'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)

# make swing_miss column
kershaw['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in kershaw['description']]

kershaw.to_csv('./data/clayton-kershaw.csv')

playerid_lookup('scherzer', 'max')

ms = statcast_pitcher('2021-04-01', '2021-05-30', 453286)
ms2 = statcast_pitcher_spin.statcast_pitcher_spin('2021-05-31','2021-10-04', 453286)
scherzer = pd.concat([ms, ms2])
# print(scherzer.shape)

scherzer.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                         'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                         'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                         'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                         'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                         'post_fld_score'], inplace = True)

scherzer['is_strike'] = [1 if x != 'B' else 0 for x in scherzer['type']]
scherzer['pitch_count'] = scherzer[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

scherzer['plate_-x'] = -scherzer['plate_x']
scherzer['pfx_-x'] = -scherzer['pfx_x']
scherzer['pfx_-x'] = 12 * scherzer['pfx_-x']
scherzer['pfx_z'] = 12 * scherzer['pfx_z']

scherzer['spin_eff'] =  round(np.cos(np.radians(scherzer['theta'])), 2)
scherzer['true_spin'] = scherzer['release_spin_rate'] * scherzer['spin_eff']

scherzer['bauer_units'] = scherzer['release_spin_rate'] / scherzer['release_speed']

scherzer['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                                ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)

scherzer['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                            'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)

scherzer['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in scherzer['description']]

scherzer.to_csv('./data/max-scherzer.csv')

playerid_lookup('kimbrel', 'craig')

craig = statcast_pitcher('2021-04-01', '2021-08-31', 518886)
craig2 = statcast_pitcher_spin.statcast_pitcher_spin('2021-09-01','2021-10-04', 518886)
kimbrel = pd.concat([craig, craig2])
# print(kimbrel.shape)

kimbrel.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                        'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                        'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                        'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                        'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                        'post_fld_score'], inplace = True)

kimbrel['is_strike'] = [1 if x != 'B' else 0 for x in kimbrel['type']]
kimbrel['pitch_count'] = kimbrel[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

kimbrel['plate_-x'] = -kimbrel['plate_x']
kimbrel['pfx_-x'] = -kimbrel['pfx_x']
kimbrel['pfx_-x'] = 12 * kimbrel['pfx_-x']
kimbrel['pfx_z'] = 12 * kimbrel['pfx_z']

kimbrel['spin_eff'] =  round(np.cos(np.radians(kimbrel['theta'])), 2)
kimbrel['true_spin'] = kimbrel['release_spin_rate'] * kimbrel['spin_eff']

kimbrel['bauer_units'] = kimbrel['release_spin_rate'] / kimbrel['release_speed']

kimbrel['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                               ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)

kimbrel['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                           'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)

kimbrel['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in kimbrel['description']]

kimbrel.to_csv('./data/craig-kimbrel.csv')

playerid_lookup('doolittle', 'sean')

sd = statcast_pitcher('2021-04-01', '2021-07-30', 448281)
sd2 = statcast_pitcher_spin.statcast_pitcher_spin('2021-07-31','2021-10-04', 448281)
doolittle = pd.concat([sd, sd2])
# print(doolittle.shape)

doolittle.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                        'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                        'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                        'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                        'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                        'post_fld_score'], inplace = True)

doolittle['is_strike'] = [1 if x != 'B' else 0 for x in doolittle['type']]
doolittle['pitch_count'] = doolittle[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

doolittle['plate_-x'] = -doolittle['plate_x']
doolittle['pfx_-x'] = -doolittle['pfx_x']
doolittle['pfx_-x'] = 12 * doolittle['pfx_-x']
doolittle['pfx_z'] = 12 * doolittle['pfx_z']

doolittle['spin_eff'] =  round(np.cos(np.radians(doolittle['theta'])), 2)
doolittle['true_spin'] = doolittle['release_spin_rate'] * doolittle['spin_eff']

doolittle['bauer_units'] = doolittle['release_spin_rate'] / doolittle['release_speed']

doolittle['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                                 ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)

doolittle['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                             'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)

doolittle['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in doolittle['description']]

doolittle.to_csv('./data/sean-doolittle.csv')

# Hitters

playerid_lookup('harper', 'bryce')

harper = statcast_batter('2021-04-01', '2021-10-04', 547180)
#print(harper.shape)

harper.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                       'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                       'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                       'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                       'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                       'post_fld_score'], inplace = True)

harper['is_strike'] = [1 if x != 'B' else 0 for x in harper['type']]
harper['pitch_count'] = harper[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

harper['plate_-x'] = -harper['plate_x']
harper['pfx_-x'] = -harper['pfx_x']
harper['pfx_-x'] = 12 * harper['pfx_-x']
harper['pfx_z'] = 12 * harper['pfx_z']

harper['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                              ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)

harper['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                          'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)

harper['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in harper['description']]

# Feature engineer first_pitch_take column by taking count and if pitch was called a strike
harper['first_pitch_take'] = [1 if x == '0-0' and y == 'called_strike' else 0 for (x, y) 
                              in zip(harper['pitch_count'], harper['description'])]
# feature engineer first_pitch_swing column by taking count, if launch speed is > 0 or if swing_miss = 1
harper['first_pitch_swing'] = [1 if x == '0-0' and (y > 0 or z > 0) else 0 for (x, y, z) 
                               in zip(harper['pitch_count'], harper['launch_speed'], harper['swing_miss'])]

harper.to_csv('./data/bryce-harper.csv')

playerid_lookup('swanson', 'dansby')

swanson = statcast_batter('2021-04-01', '2021-10-04', 621020)
#print(swanson.shape)

swanson.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                        'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                        'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                        'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                        'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                        'post_fld_score'], inplace = True)

swanson['is_strike'] = [1 if x != 'B' else 0 for x in swanson['type']]
swanson['pitch_count'] = swanson[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

swanson['plate_-x'] = -swanson['plate_x']
swanson['pfx_-x'] = -swanson['pfx_x']
swanson['pfx_-x'] = 12 * swanson['pfx_-x']
swanson['pfx_z'] = 12 * swanson['pfx_z']

swanson['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                               ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)

swanson['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                           'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)

swanson['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in swanson['description']]

swanson['first_pitch_take'] = [1 if x == '0-0' and y == 'called_strike' else 0 for (x, y) 
                               in zip(swanson['pitch_count'], swanson['description'])]

swanson['first_pitch_swing'] = [1 if x == '0-0' and (y > 0 or z > 0) else 0 for (x, y, z) 
                                in zip(swanson['pitch_count'], swanson['launch_speed'], swanson['swing_miss'])]

swanson.to_csv('./data/dansby-swanson.csv')

playerid_lookup('gallo', 'joey')

gallo = statcast_batter('2021-04-01', '2021-10-04', 608336)
#print(gallo.shape)

gallo.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                      'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                      'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                      'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                      'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                      'post_fld_score'], inplace = True)

gallo['is_strike'] = [1 if x != 'B' else 0 for x in gallo['type']]
gallo['pitch_count'] = gallo[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

gallo['plate_-x'] = -gallo['plate_x']
gallo['pfx_-x'] = -gallo['pfx_x']
gallo['pfx_-x'] = 12 * gallo['pfx_-x']
gallo['pfx_z'] = 12 * gallo['pfx_z']

gallo['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                             ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)

gallo['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                         'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)

gallo['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in gallo['description']]

gallo['first_pitch_take'] = [1 if x == '0-0' and y == 'called_strike' else 0 for (x, y) 
                             in zip(gallo['pitch_count'], gallo['description'])]

gallo['first_pitch_swing'] = [1 if x == '0-0' and (y > 0 or z > 0) else 0 for (x, y, z) 
                              in zip(gallo['pitch_count'], gallo['launch_speed'], gallo['swing_miss'])]

gallo.to_csv('./data/joey-gallo.csv')

