import cufflinks as cf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot
from plotly.subplots import make_subplots
from config import settings

# Initialize offline capability
cf.go_offline()

class NetflixVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_show_type_frequency(self):
        """Generates content type breakdown bar layout."""
        type_of_shows = self.df["type"].value_counts()
        fig = px.bar(
            data_frame=type_of_shows,
            x=type_of_shows.index,
            y=type_of_shows,
            color=type_of_shows.index,
            color_discrete_sequence=[settings.COLOR_SECONDARY, settings.COLOR_PRIMARY],
            text_auto=True,
            title="Show Type Frequency",
            labels={"y": "Frequency", "index": "Show Type"},
        )
        fig.update_traces(insidetextfont={"family": settings.FONT_FAMILY, "size": 15})
        iplot(fig)

    def plot_content_distribution_pie(self):
        """Generates distribution pie chart."""
        type_counts = self.df["type"].value_counts().reset_index()
        fig = px.pie(
            type_counts,
            values="count",
            names="type",
            title="Content Distribution: Movies vs TV Shows",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        fig.show()

    def plot_top_countries(self):
        """Generates top 10 content producing countries horizontal chart."""
        top_countries = (
            self.df[self.df["country"] != "Not Given"]["country"]
            .value_counts()
            .head(10)
            .reset_index()
        )
        fig = px.bar(
            top_countries,
            x="count",
            y="country",
            orientation="h",
            title="Top 10 Content Producing Countries",
            labels={"count": "Total Shows/Movies", "country": "Country"},
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        fig.show()

    def plot_release_trends(self):
        """Generates line trend for historical content output."""
        yearly_content = (
            self.df["release_year"].value_counts().reset_index().sort_values("release_year")
        )
        fig = px.area(
            yearly_content,
            x="release_year",
            y="count",
            title="Evolution of Content Release Years",
            labels={"release_year": "Year of Release", "count": "Number of Releases"},
        )
        fig.show()

    def plot_maturity_ratings(self):
        """Generates Treemap structure for age targets."""
        rating_counts = self.df["rating"].value_counts().reset_index()
        fig = px.treemap(
            rating_counts,
            path=["rating"],
            values="count",
            title="Audience Breakdown by Maturity Rating",
            color="count",
            color_continuous_scale="Purples",
        )
        fig.show()

    def generate_unified_dashboard(self):
        """Assembles a composite dashboard layout grid."""
        type_counts = self.df["type"].value_counts().reset_index()
        top_countries = self.df[self.df["country"] != "Not Given"]["country"].value_counts().head(10).reset_index()
        yearly_content = self.df["release_year"].value_counts().reset_index().sort_values("release_year")
        rating_counts = self.df["rating"].value_counts().reset_index()

        dashboard = make_subplots(
            rows=2, cols=2,
            specs=[[{"type": "domain"}, {"type": "xy"}],
                   [{"type": "xy"}, {"type": "domain"}]],
            subplot_titles=('Movies vs TV Shows', 'Top 10 Countries', 'Release Trends', 'Maturity Ratings')
        )

        dashboard.add_trace(go.Pie(labels=type_counts["type"], values=type_counts["count"]), row=1, col=1)
        dashboard.add_trace(go.Bar(x=top_countries["count"], y=top_countries["country"], orientation="h"), row=1, col=2)
        dashboard.add_trace(go.Scatter(x=yearly_content["release_year"], y=yearly_content["count"], fill="tozeroy"), row=2, col=1)
        dashboard.add_trace(go.Treemap(labels=rating_counts["rating"], parents=[""]*len(rating_counts), values=rating_counts["count"]), row=2, col=2)

        dashboard.update_layout(height=800, width=1000, title_text="Streaming Data Insights Dashboard", showlegend=False)
        iplot(dashboard)
