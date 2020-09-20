# Generated by Django 3.1 on 2020-09-19 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaguesettings',
            options={'ordering': ('title',), 'verbose_name_plural': 'League Settings'},
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='league_hosting_site',
            field=models.CharField(choices=[('espn', 'ESPN'), ('yahoo', 'Yahoo'), ('other', 'Other')], max_length=20, verbose_name='Hosting Site'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='number_of_teams',
            field=models.IntegerField(verbose_name='Number of Teams'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='passing_interceptions',
            field=models.FloatField(verbose_name='Points Per Interception'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='passing_touchdowns',
            field=models.FloatField(verbose_name='Points Per Passing Touchdown'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='passing_two_point_conversions',
            field=models.FloatField(verbose_name='Points Per Passing Two Point Conversion'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='passing_yards',
            field=models.FloatField(verbose_name='Points Per Passing Yard'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_bench_spots',
            field=models.IntegerField(verbose_name='Bench Spots'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_cornerbacks',
            field=models.IntegerField(verbose_name='Cornerbacks'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_defensive_backs',
            field=models.IntegerField(verbose_name='Defensive Backs'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_defensive_ends',
            field=models.IntegerField(verbose_name='Defensive Ends'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_defensive_lines',
            field=models.IntegerField(verbose_name='Defensive Lines'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_defensive_players',
            field=models.IntegerField(verbose_name='Defensive Players'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_defensive_tackles',
            field=models.IntegerField(default=0, verbose_name='Defensive Tackles'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_edge_rushers',
            field=models.IntegerField(verbose_name='Edge Rushers'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_flex_running_back_wide_receiver',
            field=models.IntegerField(verbose_name='Flex RB/WR'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_flex_running_back_wide_receiver_tight_end',
            field=models.IntegerField(verbose_name='Flex RB/WR/TE'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_flex_wide_receiver_tight_end',
            field=models.IntegerField(verbose_name='Flex WR/TE'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_head_coaches',
            field=models.IntegerField(verbose_name='Head Coaches'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_injured_reserve_spots',
            field=models.IntegerField(verbose_name='Injured Reserve Spots'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_kickers',
            field=models.IntegerField(verbose_name='Kickers'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_linebackers',
            field=models.IntegerField(verbose_name='Linebackers'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_offensive_players',
            field=models.IntegerField(verbose_name='Offensive Players'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_punters',
            field=models.IntegerField(verbose_name='Punters'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_quarterbacks',
            field=models.IntegerField(verbose_name='Quarterbacks'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_running_backs',
            field=models.IntegerField(verbose_name='Running Backs'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_safeties',
            field=models.IntegerField(verbose_name='Safeties'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_team_defense_special_teams',
            field=models.IntegerField(verbose_name='Defense / Special Teams'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_team_quarterbacks',
            field=models.IntegerField(verbose_name='Team Quarterbacks'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_tight_ends',
            field=models.IntegerField(verbose_name='Tight Ends'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='roster_wide_receivers',
            field=models.IntegerField(verbose_name='Wide Receivers'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='rushing_touchdowns',
            field=models.FloatField(verbose_name='Points Per Rushing Touchdown'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='rushing_two_point_conversions',
            field=models.FloatField(verbose_name='Points Per Rushing Two Point Conversion'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='rushing_yards',
            field=models.FloatField(verbose_name='Points Per Rushing Yard'),
        ),
        migrations.AlterField(
            model_name='leaguesettings',
            name='title',
            field=models.CharField(max_length=50, verbose_name='fantaSheet Name'),
        ),
    ]